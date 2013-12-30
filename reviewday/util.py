import json
import os
import tempfile
import html_helper
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

    with tempfile.NamedTemporaryFile(dir=out_dir, delete=False) as f:
        json.dump(data, f, indent=2)
    os.rename(f.name, os.path.join(out_dir, 'reviewday.json'))


def create_report(out_dir, name_space={}):
    filename = os.path.join(os.path.dirname(__file__), 'report.html')
    report_text = open(filename).read()
    name_space['helper'] = html_helper
    t = Template(report_text, searchList=[name_space])

    prep_out_dir(out_dir)

    out_file = open(os.path.join(out_dir, 'index.html'), "w")
    out_file.write(str(t))
    out_file.close()

    _create_json(out_dir, name_space=name_space)
