import pulumi
import pulumi_github as github

goodguygroves_github_io = github.Repository("goodguygroves.github.io",
    allow_auto_merge=False,
    allow_merge_commit=True,
    allow_rebase_merge=True,
    allow_squash_merge=True,
    archived=False,
    delete_branch_on_merge=False,
    description="Personal Website",
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    name="goodguygroves.github.io",
    pages=github.RepositoryPagesArgs(
        cname="defruss.com",
        source=github.RepositoryPagesSourceArgs(
            branch="master",
        ),
    ),
    opts=pulumi.ResourceOptions(protect=True))

