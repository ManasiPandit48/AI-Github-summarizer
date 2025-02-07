# github_api/issues.py
from github import Github
from app.ai_utils import TextAnalysisTool

def summarize_issues(repo_name):
    repo = Github().get_repo(repo_name)
    issues = repo.get_issues(labels=["good first issue", "help wanted"])
    tool = TextAnalysisTool(model_type="gpt4all", model_path="path_to_gpt4all_model")
    summaries = []
    for issue in issues:
        summary = tool.generate_description(issue.title + ": " + issue.body)
        summaries.append(summary)
    return summaries