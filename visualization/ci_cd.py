# visualization/ci_cd.py
import os
import yaml
from graphviz import Digraph

def parse_ci_cd_workflows(repo_path):
    """
    Parses .github/workflows/*.yml files to extract CI/CD workflows.
    """
    workflows = []
    workflows_dir = os.path.join(repo_path, ".github", "workflows")
    
    if os.path.exists(workflows_dir):
        for file in os.listdir(workflows_dir):
            if file.endswith(".yml") or file.endswith(".yaml"):
                with open(os.path.join(workflows_dir, file), "r") as f:
                    try:
                        workflow = yaml.safe_load(f)
                        workflows.append(workflow)
                    except yaml.YAMLError as e:
                        print(f"Error parsing YAML file {file}: {e}")
    return workflows

def visualize_ci_cd(workflows):
    """
    Visualizes CI/CD workflows using Graphviz.
    """
    dot = Digraph(comment="CI/CD Workflow")
    
    for i, workflow in enumerate(workflows):
        workflow_name = workflow.get("name", f"Workflow {i+1}")
        dot.node(workflow_name, label=workflow_name)
        
        # Parse jobs and their dependencies
        jobs = workflow.get("jobs", {})
        for job_name, job_config in jobs.items():
            dot.node(job_name, label=job_name)
            dot.edge(workflow_name, job_name)
            
            # Add steps as sub-nodes
            steps = job_config.get("steps", [])
            for step in steps:
                step_name = step.get("name", "Unnamed Step")
                dot.node(step_name, label=step_name)
                dot.edge(job_name, step_name)
    
    return dot