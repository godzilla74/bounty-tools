import argparse
import re

parser = argparse.ArgumentParser(description='')
parser.add_argument('--infile', help="File of urls to check (in format http(s)://example.com)", required=True)
parser.add_argument('--outfile', help="Where to save the results", required=True)
parser.add_argument('--domain', help="The domain to filter out (example.com)", required=True)
parser.add_argument('--exclude', help="Extensions to exclude ('.png .jpg .jpeg .svg .gif' by default)", nargs="+")
args = parser.parse_args()

if not args.exclude or len(args.exclude) == 0:
    exclusions = [".png",".jpg",".jpeg",".svg",".gif","woff","ttf"]
else:
    exclusions = args.exclude

blacklist = re.compile('|'.join([re.escape(word) for word in exclusions]))

endList = list()
linkList = list()

linkList = [line.strip('\n').lower() for line in open(args.infile, 'r')]
linkList = list(dict.fromkeys(linkList))

for url in linkList:
    exts = url.split("/")
    sIndex = [exts.index(i) for i in exts if args.domain in i]
    for e in exts[sIndex[0]+1:]:
        if not blacklist.search(e):
            e = "/{}".format(e)
            if e not in endList:
                print("[+] Adding: {}".format(e))
                endList.append(e)

f = open(args.outfile, "a")
for e in endList:
    f.write("{}\n".format(e))

print("[!] Complete")
print("[!] Wordlist saved to {}".format(args.outfile))
