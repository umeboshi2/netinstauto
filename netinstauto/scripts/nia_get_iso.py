import os
import argparse
import subprocess
import hashlib
import requests

from ..util import extract_iso, extract_bootblock

from ..preseeder import get_template

netinst_url = 'https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/9.5.0+nonfree/amd64/iso-cd/firmware-9.5.0-amd64-netinst.iso' # noqa

url_root = "https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/{version}/{arch}/iso-cd" # noqa


print(url_root.format(version='foo', arch='sdfsd'))

def check_file_sha256(filename, sha256):
    ck = hashlib.new('sha256')
    ck.update(open(filename, 'rb').read())
    return sha256 == ck.hexdigest()

def get_remote_checksum(urlroot):
    sha_url = os.path.join(urlroot, 'SHA256SUMS')
    res = requests.get(sha_url)
    line = res.content.decode().strip()
    sha256, filename = line.split()
    return sha256, filename

def download_file(url, filename):
    res = requests.get(url, stream=True)
    with open(filename, 'wb') as outfile:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                outfile.write(chunk)
    return filename

def main():
    url = args.url
    debversion = args.debversion
    arch = args.arch
    sha256 = None
    if url is None:
        dirname = url_root.format(version=args.debversion, arch=args.arch)
        sha256, filename = get_remote_checksum(dirname)
        url = os.path.join(dirname, filename)
    else:
        filename = os.path.basename(args.url)
        sha256, filename = get_remote_checksum(os.path.dirname(args.url))
    if not os.path.isfile(filename):
        print("Downloading {}.".format(filename))
        download_file(url, filename)
    if not os.path.isfile(filename):
        raise RuntimeError("{} is absent!".format(filename))
    else:
        if check_file_sha256(filename, sha256):
            print("{} is present.".format(filename))
        else:
            raise RuntimeError("Bad iso checksum for {}".format(filename))
    extract_iso(filename)
    extract_bootblock(filename)
    get_template()
    return 0


parser = argparse.ArgumentParser()
parser.add_argument('--url', default=None)
parser.add_argument('--debversion', default='current')
parser.add_argument('--arch', default='amd64')
args = parser.parse_args()
