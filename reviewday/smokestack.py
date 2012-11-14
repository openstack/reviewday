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
                    if data['nova_revision'] and \
                            data['nova_revision'][:7] == git_hash:
                        jobs_with_hash.append(job)
                    if data['glance_revision'] and \
                            data['glance_revision'][:7] == git_hash:
                        jobs_with_hash.append(job)
                    if data['keystone_revision'] and \
                            data['keystone_revision'][:7] == git_hash:
                        jobs_with_hash.append(job)
                    if data['swift_revision'] and \
                            data['swift_revision'][:7] == git_hash:
                        jobs_with_hash.append(job)
                    if data['cinder_revision'] and \
                            data['cinder_revision'][:7] == git_hash:
                        jobs_with_hash.append(job)
                    if data['quantum_revision'] and \
                            data['quantum_revision'][:7] == git_hash:
                        jobs_with_hash.append(job)
            return jobs_with_hash
        else:
            return self._jobs
