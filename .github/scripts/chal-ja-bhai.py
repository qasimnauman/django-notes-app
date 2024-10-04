# File: .github/scripts/merge_dependabot_prs.py

import os
from github import Github

def process_pr(pr):
    print(f"Processing PR #{pr.number}: {pr.title}")
    try:
        pr.create_review(event="APPROVE")
        print(f"Approved PR #{pr.number}")
        pr.merge(merge_method="squash")
        print(f"Merged PR #{pr.number}")
    except Exception as e:
        print(f"Error processing PR #{pr.number}: {str(e)}")

def main():
    g = Github(os.environ['GITHUB_TOKEN'])
    repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])

    dependabot_prs = [pr for pr in repo.get_pulls(state='open') 
                      if pr.user.login == 'dependabot[bot]' and pr.title.startswith('Bump ')]

    if not dependabot_prs:
        print("No open Dependabot PRs found to merge.")
    else:
        for pr in dependabot_prs:
            process_pr(pr)

if __name__ == "__main__":
    main()
