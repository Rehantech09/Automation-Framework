import requests

class ProjectAPI:
    def __init__(self):
        self.base_url = "https://company1.workflowpro.com/api/v1"
        self.headers = {
            "Authorization": "Bearer dummy-token",
            "X-Tenant-ID": "company1"
        }

    def create_project(self, name):
        payload = {
            "name": name,
            "description": "Test project created via API"
        }

        # Dummy response (mocked for assignment)
        return {
            "id": 123,
            "name": name,
            "status": "active"
        }