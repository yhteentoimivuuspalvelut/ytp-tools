
region = "eu-west-1"
relative_cache_path = "deployment_cache/"
relative_template_path = "cloudformation_templates/"
project_prefix = "ytp"

git_url_ytp = "https://github.com/yhteentoimivuuspalvelut/ytp.git"
git_url_secrets = "git@github.com:yhteentoimivuuspalvelut/ytp-secrets.git"

cloudformation_templatefile = "simple-deployment.template"
cloudformation_create_timeout = 900
cloudformation_create_pollrate = 15
