import re
import requests
import argparse
import urllib3
from urllib.parse import urlparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--infile', help="File of urls to check (in format http(s)://example.com)", required=True)
parser.add_argument('--outfile', help="Where to save the results", required=True)
parser.add_argument('--payload', help="The payload to replace parameter values with", required=True)
args = parser.parse_args()

payload = args.payload
f = open(args.outfile, "a")

def gen_payload_with_prefix(req_type, link):
    """ appends the request type to the given payload """
    regex = re.compile("(?<=\=)([^&\s+]*)(?=&)?")
    link = re.sub(regex, r"{}.{}.{}".format(req_type, urlparse(link).netloc, payload), link.rstrip())
    return link

def search_headers(headers):
    """ search for payload in response headers """
    if headers:
        res = [val for key, val in headers.items() if payload in val]
        if res:
            return headers
    else:
        return None

def send_request(req_type, url):
    if payload in url:
        try:
            r = requests.get(url)
            print("[+] Sent get request to {}".format(url))
            return r.headers
        except requests.exceptions.ConnectionError:
            print("[!] Failed to send request to {}".format(url))
    else:
        print("[!] Skipped request due to lack of parameters in {}".format(url))

def main():
    urls = list()
    urls = [line.strip("\n") for line in open(args.infile, "r")]
    for url in urls:
        url = gen_payload_with_prefix("get", url)
        headers = send_request("get", url)
        result = search_headers(headers)
        if result is not None:
            print("[+] Found reflected parameter(s) from {} in headers:\n\t{}".format(url, result))
            f.write("{}\t{}".format(url, result))
        else:
            print("[-] Found nothing reflected in headers for {}".format(url))

if __name__ == "__main__":
    main()
