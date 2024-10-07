import os
import subprocess

def update():
    """
    This function updates the current directory by fetching the latest
    code from the GitHub repository.
    """
    try:
        if not os.path.exists(".git"):
            print("Error: This directory is not a Git repository.")
            return
        print("Fetching the latest updates from GitHub...")
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)
        if "Already up to date" in result.stdout:
            print("Your scripts are already up-to-date.")
        else:
            print(result.stdout)
            print("Update complete. Your scripts have been updated.")

    except Exception as e:
        print(f"An error occurred during the update: {e}")

if __name__ == "__main__":
    update()
