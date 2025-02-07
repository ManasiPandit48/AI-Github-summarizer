# security/scanner.py
import subprocess

def run_security_scan(repo_path):
    """
    Runs TruffleHog to scan for secrets in the repository.
    """
    try:
        result = subprocess.run(
            ["trufflehog", "git", repo_path],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error during scan: {result.stderr}"
    except Exception as e:
        return f"Failed to run security scan: {str(e)}"