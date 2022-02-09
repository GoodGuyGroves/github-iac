import pulumi
import pulumi_github as github

familytreerecipes = github.Repository("familytreerecipes",
    allow_auto_merge=False,
    allow_merge_commit=True,
    allow_rebase_merge=True,
    allow_squash_merge=True,
    archived=False,
    delete_branch_on_merge=False,
    description="A recipe book made from family recipes.",
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    name="familytreerecipes",
    opts=pulumi.ResourceOptions(protect=True))

