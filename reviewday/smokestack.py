import json
import httplib2


class SmokeStack(object):

    def __init__(self, url):
        self._jobs = None
        self.url = url

    def jobs(self, git_hash=None):
        if not self._jobs:
            h = httplib2.Http()
            resp, content = h.request(self.url, "GET")
            self._jobs = json.loads(content)
        if git_hash:
            jobs_with_hash = []
            for job in self._jobs:
                for job_type, data in job.iteritems():
                    if data['nova_revision'] == git_hash or \
                        data['glance_revision'] == git_hash or \
                        data['keystone_revision'] == git_hash:
                        jobs_with_hash.append(job)
            return jobs_with_hash
        else:
            return self._jobs
