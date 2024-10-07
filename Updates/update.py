#!/usr/bin/env python3

# Library Imports
import os
import subprocess


# Check for updates in the github repo of CryptHound
def update():
    """
    This function updates the entire CryptHound directory by fetching the latest
    code from the GitHub repository using Git commands.
    """

    repoPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
    try:
        os.chdir(repoPath)
        if not os.path.exists(os.path.join(repoPath, ".git")):
            print("Error: This directory is not a Git repository.")
            print("Please clone the repository first.")
            return
        
        print("Fetching the latest updates ...")

        updates = subprocess.run(["git", "pull"], capture_output = True, text = True)
        if "Already up to date." in updates.stdout:
            print("Your repository is already up-to-date.")
        else:
            print("Update complete.")

    except Exception as error:
        print(f"An error occurred during the update: {error}")

if __name__ == "__main__":
    update()
