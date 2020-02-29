import requests
import argparse
import urllib3
from urllib.parse import urlparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser(description='')
parser.add_argument('--infile', help="File of urls to check (in format http(s)://example.com)", required=True)
parser.add_argument('--outfile', help="Where to save the results", required=True)
parser.add_argument('--params', help="The parameters to force", nargs="+", required=True)
parser.add_argument('--payload', help="The payload to replace parameter values with", required=True)
args = parser.parse_args()

params = args.params
payload = args.payload
f = open(args.outfile, "a")

def request_agent(req_type, url):
    base_url = urlparse(url).netloc
    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': agent, 'Host': base_url}
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

def gen_payload_with_params(req_type, url):
    for i, p in enumerate(params):
        if i == 0:
            url = url + "?{}={}".format(p, payload)
        else:
            url = url + "&{}={}".format(p, payload)
    return url


def main():
    urls = list()
    urls = [line.strip("\n") for line in open(args.infile, "r")]

    for url in urls:
        request_agent("get", gen_payload_with_params("get", url))
        request_agent("post", gen_payload_with_params("post", url))

if __name__ == "__main__":
    main()
