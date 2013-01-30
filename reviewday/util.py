import os
import html_helper
from Cheetah.Template import Template
from distutils.dir_util import copy_tree


def prep_out_dir(out_dir):
    src_dir = os.path.dirname(__file__)
    report_files_dir = os.path.join(src_dir, 'report_files')
    copy_tree(report_files_dir, out_dir)


def create_report(out_dir, name_space={}):
    filename = os.path.join(os.path.dirname(__file__), 'report.html')
    report_text = open(filename).read()
    name_space['helper'] = html_helper
    t = Template(report_text, searchList=[name_space])

    prep_out_dir(out_dir)

    out_file = open(os.path.join(out_dir, 'index.html'), "w")
    out_file.write(str(t))
    out_file.close()
