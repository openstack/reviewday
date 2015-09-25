class MergeProp(object):

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

    def _calc_score(self, lp, cur_timestamp):
        cause = 'No link'
        try:
            if self.topic.find('bug/') == 0:
                bug = lp.bug(self.topic[4:])
                # FIXME: bug.importance doesn't seem to work but it should?
                cause = '%s bugfix' % bug.bug_tasks[0].importance
            elif self.topic.find('bp/') == 0:
                spec = lp.specification(self.project, self.topic[3:])
                if spec:
                    cause = '%s feature' % spec.priority
            else:
                spec = lp.specification(self.project, self.topic)
                if spec:
                    cause = '%s feature' % spec.priority
        except:
            print 'WARNING: unable to find cause for %s' % self.topic
            cause = 'No link'

        if cause not in MergeProp.cause_score:
            print 'WARNING: unable to find score for ' \
                  '(%s, %s)' % (self.topic, cause)
            return ("No link", "Unknown cause: " + cause, 0)
        score = MergeProp.cause_score[cause]
        reason = [cause + " (+%d)" % (score)]
        # Add a score based on the time the patch has been waiting for approval
        days_old = int((cur_timestamp - self.revisionCreatedOn) / 86400)
        if ((days_old > 0) and (self.lowest_feedback != -2)):
            # A medium bugfix will have to be around for 10 days before it is
            # ranked higher than a low feature.
            days_old_score = 3 * days_old
            reason.append("%d days old (+%d)" % (days_old, days_old_score))
            score = score + days_old_score
        return (cause, reason, score)

    def __init__(self, lp, review, cur_timestamp):
        self.owner_name = review['owner']['name']
        self.url = '%s/#change,%s' % tuple(review['url'].rsplit('/', 1))
        self.subject = review['subject']
        self.project = review['project'][10:]
        if 'topic' in review:
            self.topic = review['topic']
        else:
            self.topic = ''
        self.revision = review['currentPatchSet']['revision']
        self.refspec = review['currentPatchSet']['ref']
        self.revisionCreatedOn = review['currentPatchSet']['createdOn']
        self.status = review['status']
        self.number = review['number']
        self.feedback = []
        self.is_wip = False

        self.lowest_feedback = None
        self.highest_feedback = None

        for approval in review['currentPatchSet'].get('approvals', []):
            name = approval['by']['name']
            value = int(approval['value'])
            self.feedback.append('%s: %+d' % (name, value))

            self.lowest_feedback = min(self.lowest_feedback, value) or value
            self.highest_feedback = max(self.highest_feedback, value) or value

            if approval['type'] == 'Workflow' and value == -1:
                self.is_wip = True

        # Make use of the feedback in calculating the score
        cause, reason, score = self._calc_score(lp, cur_timestamp)
        self.score = score
        self.reason = reason
        self.cause = cause
        self.rank = MergeProp.cause_score[cause]
