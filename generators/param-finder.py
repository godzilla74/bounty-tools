import re
import urllib.parse
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--infile', help="File of urls to check (in format http(s)://example.com)", required=True)
parser.add_argument('--outfile', help="Where to save the results", required=True)
args = parser.parse_args()

params = []
pattern = '(\?|\&)([^=]+)\=([^&]+)'

f = open(args.outfile, 'w')

for line in open(args.infile):
    m = re.search(pattern, line)
    if m:
        unencoded = urllib.parse.unquote(m.group(2))
        if unencoded not in params:
            params.append(unencoded)
            f.write(unencoded+'\n')

f.close()
