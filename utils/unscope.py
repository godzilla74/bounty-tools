import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--ip_file', help="File with IPs (line by line)", required=True)
parser.add_argument('--out_scope', help="File with out of scope IPs", required=True)
parser.add_argument('--outfile', help="Where to save the results", required=True)
args = parser.parse_args()

ip_list = [line.strip('\n') for line in open(args.ip_file, 'r')]
out_scope_list = [line.strip('\n') for line in open(args.out_scope, 'r')]

print("Starting to prune")
good_list = [el for el in ip_list if el not in out_scope_list]
print("Prune complete")

f = open(args.outfile, 'a')
for x in good_list:
    f.write("{}\n".format(x))

print("Results written to: {}".format(args.outfile))
