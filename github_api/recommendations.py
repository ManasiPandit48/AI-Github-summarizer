# github_api/recommendations.py
from github import Github

def recommend_repositories(repo_name):
    """
    Recommends repositories based on tags/topics of the given repository.
    """
    repo = Github().get_repo(repo_name)
    topics = repo.get_topics()
    recommendations = []

    for topic in topics:
        # Search repositories by topic
        search_results = Github().search_repositories(topic)
        for result in search_results[:5]:  # Limit to top 5 results per topic
            recommendations.append({
                "name": result.full_name,
                "description": result.description,
                "url": result.html_url
            })
    return recommendations