# utils/helpers.py
import os

def load_env_variable(key, default=None):
    """
    Load an environment variable or return a default value.
    """
    return os.getenv(key, default)

def format_markdown_list(items):
    """
    Converts a list of items into a Markdown-formatted list.
    """
    if not items:
        return ""
    markdown_str = ""
    for index, item in enumerate(items, start=1):
        markdown_str += f"{index}. {item}\n"
    return markdown_str