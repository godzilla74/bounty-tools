import argparse
import ipaddress

parser = argparse.ArgumentParser(description='')
parser.add_argument('--infile', help="File with IPs in CIDR format", required=True)
parser.add_argument('--outfile', help="Where to save the results", required=True)
args = parser.parse_args()

cidrList = list()
ipList = list()

cidrList = [line.strip('\n') for line in open(args.infile, 'r')]

for c in cidrList:
  for ip in ipaddress.IPv4Network(c, strict=False):
    ipList.append(str(ip))

f = open(args.outfile, 'a')
for ip in ipList:
  f.write("{}\n".format(ip))
