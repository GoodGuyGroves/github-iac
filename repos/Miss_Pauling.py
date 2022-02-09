import pulumi
import pulumi_github as github

miss__pauling = github.Repository("Miss_Pauling",
    allow_auto_merge=False,
    allow_merge_commit=True,
    allow_rebase_merge=True,
    allow_squash_merge=True,
    archived=False,
    delete_branch_on_merge=False,
    description="Discord bot for rsa.tf/discord",
    has_downloads=True,
    has_projects=True,
    has_wiki=True,
    name="Miss_Pauling",
    opts=pulumi.ResourceOptions(protect=True))

