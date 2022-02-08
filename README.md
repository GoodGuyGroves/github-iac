# github-iac
Infrastructure-as-Code for my Github account


# Gitpod
Steps I will need to reproduce if I want to use this repo with Gitpod.io

## Prerequisites
- Configure Gitpod.io env var secret for `GITHUB_TOKEN`


## Steps
1) Install Pulumi
```
curl -fsSL https://get.pulumi.com | sh
```

2) Verify installation
```
pulumi version
```

3) Install Python PDM
```
curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -
```

4) Source ~/.bashrc to get Pulumi and PDM added to $PATH
```
source ~/.bashrc
```

5) Install all python deps
```
pdm install
```
