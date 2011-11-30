# Helper functions to help generate the HTML report


def job_data_for_type(jobs, job_type):
    """ Return a reference to the first job of the specified type. """
    for job in jobs:
        for jt, data in job.iteritems():
            if jt == job_type:
                return data


def fail_status(job_data):
    """ Return a reference to the first job of the specified type. """
    if job_data['status'] == 'Failed':
        return '<font style="color: #FF0000;">(Fail)</font>'
    elif job_data['status'] == 'Success':
        return '<font style="color: #00AA00;">(Pass)</font>'
    else:
        return ''

def review_feedback(mp):
    return '&#13'.join(mp.feedback)

def lowest_feedback(mp):
    if mp.lowest_feedback is None:
        return ''
    if mp.lowest_feedback > 0:
        color = '#00AA00'
    else:
        color = '#FF0000'
    return '<font style="color: %s;">%+d</font>' % (color, mp.lowest_feedback)
