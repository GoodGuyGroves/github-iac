import pulumi
import pulumi_github as github

dotfiles = github.Repository("dotfiles",
    allow_auto_merge=False,
    allow_merge_commit=True,
    allow_rebase_merge=True,
    allow_squash_merge=True,
    archived=False,
    delete_branch_on_merge=False,
    description="A collection of my dotfiles",
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    name="dotfiles",
    opts=pulumi.ResourceOptions(protect=True))
