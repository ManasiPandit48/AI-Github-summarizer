# visualization/contributors.py
from github import Github
import plotly.express as px

def plot_contributor_activity(repo_name):
    """
    Fetches contributor activity from a GitHub repository and visualizes it.
    """
    # Initialize GitHub API
    repo = Github().get_repo(repo_name)
    
    # Fetch contributors and their contributions
    contributors = repo.get_contributors()
    activity = {c.login: c.contributions for c in contributors}
    
    # Create a bar chart using Plotly
    fig = px.bar(
        x=list(activity.keys()),
        y=list(activity.values()),
        labels={"x": "Contributor", "y": "Number of Contributions"},
        title="Contributor Activity",
        color=list(activity.values()),  # Optional: Add color based on contributions
        color_continuous_scale="Blues"
    )
    fig.update_layout(xaxis_tickangle=-45)  # Rotate x-axis labels for better readability
    return fig