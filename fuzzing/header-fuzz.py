import requests
import argparse
import urllib3
from urllib.parse import urlparse

import pprint


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser(description='')
parser.add_argument('--infile', help="File of urls to check (in format http(s)://example.com)", required=True)
parser.add_argument('--outfile', help="Where to save the results", required=True)
parser.add_argument('--headers', help="The Header(s) to change", nargs="+", required=True)
parser.add_argument('--payload', help="The payload to replace parameter values with", required=True)
args = parser.parse_args()

headers = args.headers
payload = args.payload
f = open(args.outfile, "a")

def request_agent(req_type, url, headers):
    try:
        if req_type == "get":
            request = requests.get(url, headers=headers, verify=False)
            print("[+] Sent GET request to {}".format(url))
            f.write("Success\tGET\t{}\n".format(url))
        if req_type == "post":
            request = requests.post(url, headers=headers)
            print("[+] Sent POST request to {}".format(url))
            f.write("Success\tPOST\t{}\n".format(url))
    except requests.exceptions.ConnectionError:
        print("[!] Failed {} request to {}".format(req_type, url))
        f.write("Fail\t{}\t{}\n".format(req_type, url))
    except requests.exceptions.TooManyRedirects:
        print("[!] Too many redirects to {}".format(url))
        f.write("Fail\t{}\t{}\n".format(req_type, url))

def gen_headers(req_type, url):
    base_url = urlparse(url).netloc
    new_headers = {}
    new_headers["Host"] = base_url
    new_headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"    
    for h in headers:
        new_headers[h] = "{}.{}.{}".format(req_type, base_url, payload)
    return new_headers

def main():
    urls = list()
    urls = [line.strip("\n") for line in open(args.infile, "r")]

    for url in urls:
        request_agent("get", url, gen_headers("get", url))
        request_agent("post", url, gen_headers("post", url))

if __name__ == "__main__":
    main()
