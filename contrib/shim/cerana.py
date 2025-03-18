from jinja2 import Environment, PackageLoader, select_autoescape
from dataclasses import dataclass
import sys

@dataclass
class Service:
    index: int

def main():
    env = Environment(
        loader=PackageLoader("cerana"),
        autoescape=select_autoescape()
    )

    deploy_count = int(sys.argv[1]) # number of nodes to deploy
    

    deploy = env.get_template("ovsc-deployments.jinja2")

    svc = []
    github_workspace = sys.argv[2] # web url to github repository

    for deployment in range(1, deploy_count):
        svc.append(Service(deployment))

    out = deploy.render(svc=svc, github_workspace=github_workspace)

    print(out)


if (__name__ == "__main__"):
    main()