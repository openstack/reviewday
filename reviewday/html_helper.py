# Helper functions to help generate the HTML report


def job_data_for_type(jobs, job_type):
    """ Return a reference to the first job of the specified type. """
    for job in jobs:
        for jt, data in job.iteritems():
            if jt == job_type:
                return data


def fail_status(job_data, token):
    """ Return a reference to the first job of the specified type. """
    output = '<font style="color: #%(color)s;">%(token)s</font>'
    if job_data['status'] == 'Failed':
        color = 'FF0000'
    elif job_data['status'] == 'Success':
        color = '00AA00'
    else:
        color = '000000'
    return output % locals()

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
