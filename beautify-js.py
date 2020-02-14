import requests
import jsbeautifier
import uuid
import sys
import os
import argparse

# arguments
parser = argparse.ArgumentParser(description='Get & beautify remote js files')
parser.add_argument('infile', help='File with the URLs in it (one URL per line)')
parser.add_argument('outdir', help='Location to save the results to (will automatically save a \'js\' folder to it.')
args = parser.parse_args()

# jsbeautifier options
opts = jsbeautifier.default_options()
opts.indent_size = 2
opts.space_in_empty_paren = True

# requests headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

# make default dir
cwd = args.outdir
outdir = os.path.join(cwd, 'js')
if not os.path.exists(outdir):
    print("[+] Making store directory: " + outdir)
    os.mkdir(outdir)

# loop through the file
for u in open(args.infile, 'r'):

    print("[+] Requesting: " + u.strip())

    r = requests.get(u.strip(), headers=headers)
    
    print("[+] Status code: " + str(r.status_code))

    if r.status_code == 200:
        # a rando name for the file since the link it's friendly
        name = uuid.uuid4().hex
        fname = os.path.join(outdir, name)
        print("[+] Saving results to: " + fname);

        # the file to write to
        f = open(fname, "a")
        
        # add the url to the first line
        f.write("Requested URL: " + u.strip())
        f.write("\n")
        f.write("\n")
        
        print("[+] Beautifying js")
        js = jsbeautifier.beautify(r.text, opts)

        try:
            f.write(js)
        except UnicodeEncodeError:
            f.write(js.encode('utf-8'))

        f.close()
