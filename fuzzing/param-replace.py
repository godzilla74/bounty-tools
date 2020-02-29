import requests
import argparse
import re
from urllib.parse import urlparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--infile', help="File of urls to check (in format http(s)://example.com)", required=True)
parser.add_argument('--outfile', help="Where to save the results", required=True)
parser.add_argument('--payload', help="The payload to replace parameter values with", required=True)
args = parser.parse_args()

payload = args.payload
f = open(args.outfile, "a")

def send_get_request(link):
    """ sends a get request """
    modified_url = gen_payload_with_prefix("get", link)
    if payload in modified_url:
        try:
            request = requests.get(modified_url)
            print("[+] Sent GET request to {}".format(modified_url))
            f.write("Success\tGET\t{}\n".format(modified_url))
        except requests.exceptions.ConnectionError:
            print("[!] Failed GET request to: {}".format(modified_url))
            f.write("Fail\tGET\t{}\n".format(modified_url))
    else:
        print("[!] Skipped GET request due to lack of parameters in {}".format(modified_url))
        
def send_post_request(link):
    """ sends a post request """
    modified_url = gen_payload_with_prefix("post", link)
    if payload in modified_url:
        try:
            request = requests.post(modified_url)
            print("[+] Sent POST request to {}".format(modified_url))
            f.write("Success\tPOST\t{}\n".format(modified_url))
        except requests.exceptions.ConnectionError:
            print("[!] Failed POST request to: {}".format(modified_url))
            f.write("Fail\tPOST\t{}\n".format(modified_url))
    else:
        print("[!] Skipped POST request due to lack of parameters in {}".format(modified_url))

def gen_payload_with_prefix(req_type, link):
    """ appends the request type to the given payload """
    regex = re.compile("(?<=\=)([^&\s+]*)(?=&)?")
    link = re.sub(regex, r"{}.{}.{}".format(req_type, urlparse(link).netloc, payload), link.rstrip())
    return link

def main():
    urls = list()
    urls = [line.strip('\n') for line in open(args.infile, "r")]
    
    # gen list with new payloads in them
    for url in urls:
        send_get_request(url)
        send_post_request(url)

if __name__ == "__main__":
    main()
