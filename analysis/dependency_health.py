# analysis/dependency_health.py
import requests

def check_dependency_health(dependency_name, version):
    """
    Checks the health of a dependency by querying Libraries.io API.
    """
    LIBRARIES_IO_API_URL = f"https://libraries.io/api/pypi/{dependency_name}/versions/{version}"
    response = requests.get(LIBRARIES_IO_API_URL)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "latest_version": data.get("latest_release_number"),
            "published_at": data.get("published_at"),
            "outdated": version != data.get("latest_release_number")
        }
    else:
        return {"error": "Failed to fetch dependency health."}