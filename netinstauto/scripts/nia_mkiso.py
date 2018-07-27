import os
import argparse
import subprocess
import yaml

from ..util import set_writable_recursive
from ..util import create_new_iso
from ..preseeder import get_template


def make_preseed_content():
    template = get_template()
    config = yaml.load(open(args.preseed))
    return template.render(**config['preseed_vars'])


def create_preseed_file(filename):
    with open(filename, 'w') as outfile:
        content = make_preseed_content()
        outfile.write(content)


def main():
    set_writable_recursive(args.working_dir)
    preseed_filename = os.path.join(args.working_dir, 'preseed.cfg')
    create_preseed_file(preseed_filename)
    create_new_iso('remastered.iso', working_dir=args.working_dir)
    return 0


parser = argparse.ArgumentParser()
parser.add_argument('--working-dir', '-w', default='netinst')
parser.add_argument('--preseed', '-p', default='preseed.yaml')
args = parser.parse_args()
