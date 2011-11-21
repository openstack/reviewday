import subprocess
import json


def reviews(project, status="open", branch="master"):
    arr = []
    cmd = 'ssh review gerrit' \
           ' query "status: %s project: openstack/%s branch: %s"' \
           ' --current-patch-set --format JSON' \
           % (status, project, branch)
    p = subprocess.Popen([cmd], shell=True, stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = p.stdout
    for line in stdout.readlines():
        review = json.loads(line)
        if 'project' in review:
            arr.append(review)

    return arr
