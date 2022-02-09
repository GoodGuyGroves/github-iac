import pulumi
import pulumi_github as github

latex_resume = github.Repository("latex_resume",
    allow_auto_merge=False,
    allow_merge_commit=True,
    allow_rebase_merge=True,
    allow_squash_merge=True,
    archived=False,
    delete_branch_on_merge=False,
    description="The Résumé of Russell Groves written in LaTeX",
    has_downloads=True,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    name="latex_resume",
    vulnerability_alerts=True,
    opts=pulumi.ResourceOptions(protect=True))

