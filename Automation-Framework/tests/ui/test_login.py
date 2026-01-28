import pytest
from playwright.sync_api import sync_playwright, TimeoutError

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1280, "height": 800}
        )
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def login(page, email, password):
    page.goto("https://app.workflowpro.com/login", wait_until="networkidle")
    page.fill("#email", email)
    page.fill("#password", password)
    page.click("#login-btn")

def test_user_login(page):
    login(page, "admin@company1.com", "password123")

    # Wait for dashboard navigation
    page.wait_for_url("**/dashboard", timeout=20000)

    # Wait for dynamic dashboard element
    welcome = page.locator(".welcome-message")
    welcome.wait_for(state="visible", timeout=15000)

    assert welcome.is_visible()

def test_multi_tenant_access(page):
    login(page, "user@company2.com", "password123")

    page.wait_for_url("**/dashboard", timeout=20000)

    # Wait for projects to load
    page.wait_for_selector(".project-card", timeout=20000)

    projects = page.locator(".project-card")
    count = projects.count()

    assert count > 0

    for i in range(count):
        assert "Company2" in projects.nth(i).text_content()
