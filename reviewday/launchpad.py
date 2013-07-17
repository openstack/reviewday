from launchpadlib.launchpad import Launchpad


class LaunchPad(object):

    def __init__(self):
        self.lp = Launchpad.login_anonymously('reviewday', 'production',
                                              '~/.launchpadlib-reviewday',
                                              version="devel", timeout=5)
        self.spec_cache = {}

    def bug(self, id):
        return self.lp.bugs[id]

    def project(self, id):
        return self.lp.projects[id]

    def specifications(self, project):
        if project not in self.spec_cache:
            specs = self.project(project).valid_specifications
            cache = {}
            for spec in specs:
                spec_str = str(spec)
                spec_name = spec_str[spec_str.index('+spec/') + 6:]
                cache[spec_name] = spec
            self.spec_cache[project] = cache
        return self.spec_cache[project]

    def specification(self, project, spec_name):
        specs = self.specifications(project)
        for name, spec in specs.iteritems():
            if name == spec_name:
                return spec
