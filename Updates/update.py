import os
import subprocess

def update():
    """
    This function updates the entire CryptHound directory by fetching the latest
    code from the GitHub repository using Git commands.
    """
    # Get the path to the CryptHound directory (the parent directory)
    repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    try:
        # Change to the repository directory
        os.chdir(repo_path)

        # Check if it's a Git repository
        if not os.path.exists(os.path.join(repo_path, ".git")):
            print("Error: This directory is not a Git repository.")
            print("Please clone the repository first.")
            return

        # Run the git pull command
        print("Fetching the latest updates from GitHub...")
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)

        # Check the output of the git pull command
        if "Already up to date." in result.stdout:
            print("Your repository is already up-to-date.")
        else:
            print("Update complete. New changes:")
            print(result.stdout)

    except Exception as e:
        print(f"An error occurred during the update: {e}")

if __name__ == "__main__":
    update()
