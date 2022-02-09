"""Managing GoodGuyGroves Github account with Pulumi!"""

import pulumi
import pulumi_github as github

github_iac = github.Repository("github-iac",
    allow_auto_merge=False,
    allow_merge_commit=True,
    allow_rebase_merge=True,
    allow_squash_merge=True,
    archived=False,
    delete_branch_on_merge=False,
    description="Infrastructure-as-Code for my Github account",
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    name="github-iac",
    opts=pulumi.ResourceOptions(protect=True))


pulumi.export('name', github_iac.name)
