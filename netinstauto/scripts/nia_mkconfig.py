import argparse
import subprocess
import pkg_resources


def main():
    filename = args.filename
    config = pkg_resources.resource_string('netinstauto', 'config.yaml')
    with open(filename, 'wb') as outfile:
        outfile.write(config)
    return 0


description = """\
Create an editable config for the preseed."""

parser = argparse.ArgumentParser(description=description)
parser.add_argument('--filename', default='preseed.yaml')
args = parser.parse_args()
