# app/github_utils.py
from github import Github
from app.ai_utils import TextAnalysisTool

def generate_repo_description(repo_name):
    repo = Github().get_repo(repo_name)
    code_snippets = ""
    for file in repo.get_contents(""):
        if file.type == "file" and file.name.endswith((".py", ".js")):
            code_snippets += file.decoded_content.decode() + "\n"
    tool = TextAnalysisTool(model_type="tinyllama")
    description = tool.generate_description(code_snippets)
    return description