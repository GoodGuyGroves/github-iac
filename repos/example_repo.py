"""Managing GoodGuyGroves Github account with Pulumi!"""

import pulumi
import pulumi_github as github

example_repo = github.Repository('example_repo',
    name="example_repo",
    description="example_repo",
    visibility="private",
    auto_init=True,
    allow_auto_merge=False,
    allow_merge_commit=True,
    allow_rebase_merge=True,
    allow_squash_merge=True,
    archive_on_destroy=False,
    archived=False,
    has_issues=True,
    vulnerability_alerts=False,
    gitignore_template="Python",
    license_template="gpl-3.0"
    )

example_file = github.RepositoryFile("README",
    repository=example_repo.name,
    branch="main",
    file="README.md",
    content="# Example Github Repository with Pulumi",
    commit_message="Commit from Pulumi",
    overwrite_on_create=True)

branch_main = github.BranchDefault("main",
    repository=example_repo.name,
    branch="main")

branch_dev = github.Branch("development",
    repository=example_repo.name,
    source_branch=branch_main.branch,
    branch="development")


pulumi.export('full name', example_repo.full_name)
