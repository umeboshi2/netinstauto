import argparse
import subprocess

necessary_binaries = ['xorriso', 'bsdtar', 'chmod',
                      'cpio', 'gzip', 'gunzip']

optional_binaries = ['convert', 'mogrify']


def which(binary):
    return subprocess.check_call(['which', binary], stdout=subprocess.DEVNULL)


def main():
    reqs = True
    opts = True
    for binary in necessary_binaries:
        try:
            which(binary)
        except subprocess.CalledProcessError:
            print("ERROR {} not found.".format(binary))
            reqs = False
            continue
        print("Found {}.".format(binary))
    for binary in optional_binaries:
        try:
            which(binary)
        except subprocess.CalledProcessError:
            print("WARNING {} not found.".format(binary))
            opts = False
            continue
        print("Found {}.".format(binary))
    if reqs:
        print("All required commands available.")
    if opts:
        print("All optional commands available.")
    return 0


parser = argparse.ArgumentParser()
args = parser.parse_args()
