# visualization/file_tree.py
import os
import plotly.express as px

def create_file_tree(repo_path):
    sizes = {root: sum(f.stat().st_size for f in files) 
             for root, _, files in os.walk(repo_path)}
    fig = px.treemap(
        names=list(sizes.keys()),
        parents=["" for _ in sizes],
        values=list(sizes.values())
    )
    return fig