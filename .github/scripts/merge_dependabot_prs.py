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

def is_dependabot_pr(pr):
    # Check if the PR is created by Dependabot
    if pr.user.login == 'dependabot[bot]':
        return True
    # Additional checks can be added here if needed
    return False

def main():
    g = Github(os.environ['GITHUB_TOKEN'])
    repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
    
    dependabot_prs = [pr for pr in repo.get_pulls(state='open') if is_dependabot_pr(pr)]
    
    if not dependabot_prs:
        print("No open Dependabot PRs found to merge.")
    else:
        for pr in dependabot_prs:
            process_pr(pr)

if __name__ == "__main__":
    main()
