class MergeProp(object):

    def _calc_score(self, lp, project, topic):
        cause = 'No link'
        try:
            if topic.find('bug/') == 0:
                bug = lp.bug(topic[4:])
                #FIXME: bug.importance doesn't seem to work but it should?
                cause = '%s bugfix' % bug.bug_tasks[0].importance
            elif topic.find('bp/') == 0:
                spec = lp.specification(project, topic[3:])
                if spec:
                    cause = '%s feature' % spec.priority
            else:
                spec = lp.specification(project, topic)
                if spec:
                    cause = '%s feature' % spec.priority
        except:
            print 'WARNING: unabled to find cause for %s' % topic
            cause = 'No link'

        cause_score = {
                      'Regression hotfix': 350,
                      'Critical bugfix': 340,
                      'Essential feature': 330,
                      'High feature': 230,
                      'Medium feature': 180,
                      'High bugfix': 130,
                      'Low feature': 100,
                      'Medium bugfix': 70,
                      'Low bugfix': 50,
                      'Undefined feature': 40,
                      'Wishlist bugfix': 35,
                      'Undecided bugfix': 30,
                      'Untargeted feature': 10,
                      'No link': 0,
                      }

        return (cause, cause_score[cause])

    def __init__(self, lp, smoker, review):
        self.owner_name = review['owner']['name']
        self.url = review['url']
        self.subject = review['subject']
        self.project = review['project'][10:]
        if 'topic' in review:
            self.topic = review['topic']
        else:
            self.topic = ''
        self.revision = review['currentPatchSet']['revision']
        self.refspec = review['currentPatchSet']['ref']
        self.number = review['number']
        cause, score = self._calc_score(lp, self.project, self.topic)
        self.score = score
        self.cause = cause
        self.jobs = smoker.jobs(self.revision[:7])
