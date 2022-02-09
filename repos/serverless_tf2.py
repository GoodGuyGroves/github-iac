import pulumi
import pulumi_github as github

serverless_tf2 = github.Repository("serverless-tf2",
    allow_auto_merge=False,
    allow_merge_commit=True,
    allow_rebase_merge=True,
    allow_squash_merge=True,
    archived=False,
    delete_branch_on_merge=False,
    description="TF2 hosted on AWS ECS Fargate",
    has_downloads=True,
    has_projects=True,
    has_wiki=True,
    name="serverless-tf2",
    opts=pulumi.ResourceOptions(protect=True))

