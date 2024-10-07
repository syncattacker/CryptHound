import os
import subprocess

def update():
    """
    This function updates the entire CryptHound directory by fetching the latest
    code from the GitHub repository using Git commands.
    """
    repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    try:
        os.chdir(repo_path)
        if not os.path.exists(os.path.join(repo_path, ".git")):
            print("Error: This directory is not a Git repository.")
            print("Please clone the repository first.")
            return
        print("Fetching the latest updates from GitHub...")
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)
        if "Already up to date." in result.stdout:
            print("Your repository is already up-to-date.")
        else:
            print("Update complete. New changes:")
            print(result.stdout)

    except Exception as e:
        print(f"An error occurred during the update: {e}")

if __name__ == "__main__":
    update()
