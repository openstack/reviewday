import json
import os
import html_helper
import subprocess
from Cheetah.Template import Template
from distutils.dir_util import copy_tree


def prep_out_dir(out_dir):
    src_dir = os.path.dirname(__file__)
    report_files_dir = os.path.join(src_dir, 'report_files')
    copy_tree(report_files_dir, out_dir)


def _create_json(out_dir, name_space={}):
    data = {
        'generated': name_space['dts'],
        'projects': {}, }

    projects = data['projects']

    for project_name in name_space['projects']:
        projects[project_name] = {}

        mps = name_space['projects'][project_name]
        for mp in mps:
            projects[project_name][mp.url] = {
                'score': mp.score,
                'cause': mp.cause,
                'subject': mp.subject,
                'owner': mp.owner_name,
                'feedback': {'lowest': mp.lowest_feedback,
                             'highest': mp.highest_feedback, }, }

    with open(os.path.join(out_dir, 'reviewday.json.tmp'), "w") as f:
        json.dump(data, f, indent=2)
    os.rename(f.name, os.path.join(out_dir, 'reviewday.json'))


def _create_data_html(out_dir, name_space={}):
    # create the full report
    filename = os.path.join(os.path.dirname(__file__), 'data_table.html')
    report_text = open(filename).read()
    name_space['helper'] = html_helper
    t = Template(report_text, searchList=[name_space])

    prep_out_dir(out_dir)

    data_table_text = str(t)
    with open(os.path.join(out_dir, 'data_table.html.tmp'), "w") as f:
        f.write(data_table_text)
    os.rename(f.name, os.path.join(out_dir, 'data_table.html'))
    return data_table_text


def create_projects_dashboard(out_dir):
    dashboard_file = '%s/milestone.dash' % out_dir
    os.system('bin/neutron -o %s' % dashboard_file)
    p = subprocess.Popen(['gerrit-dash-creator',
                         dashboard_file],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    neutron_dash, err = p.communicate()
    return {'neutron_dash': neutron_dash}


def create_report(out_dir, name_space={}):
    # create html partial with just the unstyled data
    data_table_text = _create_data_html(out_dir, name_space)

    # create the full report
    report_name_space = {'data': data_table_text, 'helper': html_helper}
    report_name_space.update(create_projects_dashboard(out_dir))
    filename = os.path.join(os.path.dirname(__file__), 'report.html')
    report_text = open(filename).read()
    t = Template(report_text, searchList=[report_name_space])

    with open(os.path.join(out_dir, 'index.html.tmp'), "w") as f:
        f.write(str(t))
    os.rename(f.name, os.path.join(out_dir, 'index.html'))

    _create_json(out_dir, name_space=name_space)
