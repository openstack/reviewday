from launchpadlib.launchpad import Launchpad


class LaunchPad(object):

    def __init__(self):
        self.lp = Launchpad.login_anonymously('reviewday', 'production',
                                 '~/.launchpadlib-reviewday', version="devel")
        self.spec_cache = {}

    def bug(self, id):
        return self.lp.bugs[id]

    def project(self, id):
        return self.lp.projects[id]

    def specifications(self, project):
        if project not in self.spec_cache:
            specs = self.project(project).valid_specifications
            self.spec_cache[project] = specs
        return self.spec_cache[project]

    def specification(self, project, spec_name):
        specs = self.specifications(project)
        for spec in specs:
            if spec.name == spec_name:
                return spec
