import json
import httplib2


class SmokeStack(object):

    def __init__(self, url):
        self._jobs = None
        self._config_templates = None
        self.url = url

    def jobs(self, git_hash=None):
        if not self._jobs:
            h = httplib2.Http(disable_ssl_certificate_validation=True)
            jobs_url = self.url + '/jobs.json?limit=99999'
            resp, content = h.request(jobs_url, "GET")
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
                    if data['neutron_revision'] and \
                            data['neutron_revision'][:7] == git_hash:
                        jobs_with_hash.append(job)
                    if data['ceilometer_revision'] and \
                            data['ceilometer_revision'][:7] == git_hash:
                        jobs_with_hash.append(job)
                    if data['heat_revision'] and \
                            data['heat_revision'][:7] == git_hash:
                        jobs_with_hash.append(job)
            return jobs_with_hash
        else:
            return self._jobs

    def config_templates(self):
        if not self._config_templates:
            h = httplib2.Http(disable_ssl_certificate_validation=True)
            ct_url = self.url + '/config_templates.json'
            resp, content = h.request(ct_url, "GET")
            self._config_templates = {}
            for ct in json.loads(content):
                self._config_templates[ct['id']] = ct['name']
        return self._config_templates
