# analysis/dependency_analyzer.py
import re
from app.ai_utils import TextAnalysisTool

def detect_dependencies(repo_files):
    dependencies = []
    for file in repo_files:
        if file.name == "requirements.txt":
            dependencies.extend(re.findall(r"^([\w-]+)==", file.decoded_content.decode()))
        elif file.name == "package.json":
            dependencies.extend(re.findall(r'"dependencies":\s*{([^}]+)}', file.decoded_content.decode()))
    tool = TextAnalysisTool(model_type="tinyllama")
    categorized_deps = tool.generate_description(", ".join(dependencies))
    return categorized_deps