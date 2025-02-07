# streamlit_app.py
import streamlit as st
from app.github_utils import generate_repo_description
from app.code_suggestions import CodeSuggestionTool
from github_api.recommendations import recommend_repositories
from utils.export_utils import generate_pdf_report, generate_excel_report
from security.scanner import run_security_scan
from visualization.contributors import plot_contributor_activity
from visualization.ci_cd import parse_ci_cd_workflows, visualize_ci_cd
from analysis.dependency_health import check_dependency_health
from utils.helpers import format_markdown_list

st.title("Repository Analyzer")

# Generate Repository Description
repo_name = st.text_input("Enter Repository Name (e.g., owner/repo):")
if st.button("Generate Description"):
    description = generate_repo_description(repo_name)
    st.write("Repository Description:")
    st.write(description)

# AI Code Suggestions
code_snippet = st.text_area("Enter Code Snippet for Suggestions:")
if st.button("Get Code Suggestions"):
    tool = CodeSuggestionTool()
    suggestions = tool.suggest_code_improvements(code_snippet)
    st.write("Code Suggestions:")
    st.write(suggestions)

# Repository Recommendations
if st.button("Get Repository Recommendations"):
    recommendations = recommend_repositories(repo_name)
    for rec in recommendations:
        st.write(f"- [{rec['name']}]({rec['url']}): {rec['description']}")

# Security Scanning
repo_path = st.text_input("Enter Local Repository Path for Security Scan:")
if st.button("Run Security Scan"):
    scan_result = run_security_scan(repo_path)
    st.text_area("Security Scan Results:", scan_result)

# Contributor Activity Visualization
if repo_name:
    if st.button("Visualize Contributor Activity"):
        fig = plot_contributor_activity(repo_name)
        st.plotly_chart(fig)

# CI/CD Workflow Visualization
if repo_path:
    if st.button("Visualize CI/CD Workflows"):
        workflows = parse_ci_cd_workflows(repo_path)
        if workflows:
            dot = visualize_ci_cd(workflows)
            st.graphviz_chart(dot.source)
        else:
            st.error("No CI/CD workflows found in the repository.")

# Dependency Health Check
dependency_name = st.text_input("Enter Dependency Name (e.g., flask):")
version = st.text_input("Enter Version (e.g., 2.0.1):")
if st.button("Check Dependency Health"):
    health_status = check_dependency_health(dependency_name, version)
    st.json(health_status)

# Export Reports
data = {"Description": "Sample Data", "Dependencies": "Flask, Pandas"}
if st.button("Export PDF Report"):
    generate_pdf_report(data)
    st.success("PDF Report Generated!")

if st.button("Export Excel Report"):
    generate_excel_report(data)
    st.success("Excel Report Generated!")