"""Managing GoodGuyGroves Github account with Pulumi!"""

import pulumi
import pulumi_github as github
from repos import (
    # example_repo,
    github_iac,
    dotfiles,
    familytreerecipes,
    latex_resume,
    serverless_tf2,
    goodguygroves_github_io,
    Miss_Pauling
)

# For importing an existing repository, run the command below
# pulumi import github:index/repository:Repository github-iac github-iac


# pulumi import github:index/repository:Repository serverless-tf2 serverless-tf2
