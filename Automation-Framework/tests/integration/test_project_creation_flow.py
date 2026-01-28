def test_project_creation_flow(api_client, page, mobile_page):
    # 1. API: Create project
    project = api_client.create_project(
        name="TestProject",
        tenant_id="company1"
    )
    project_id = project["id"]

    # 2. Web UI: Verify project appears
    page.goto("https://company1.workflowpro.com/login")
    login(page, "admin@company1.com", "password123")

    page.wait_for_selector(".project-card")

    assert page.locator(
        f"text=TestProject"
    ).is_visible()

    # 3. Mobile: Check accessibility
    mobile_page.goto("https://company1.workflowpro.com/dashboard")
    assert mobile_page.locator("text=TestProject").is_visible()

    # 4. Tenant isolation
    page.goto("https://company2.workflowpro.com/dashboard")
    assert page.locator("text=TestProject").count() == 0
