import base64
import urllib.parse
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--decode', help="Decode payload", type=bool, default=False)
parser.add_argument('--encode', help="Encode payload", type=bool, default=False)
parser.add_argument('--payload', help="The payload")
args = parser.parse_args()


def decode_string(payload):
    # remove url encoding from the original string
    decoded_request = urllib.parse.unquote(payload)
    # decode base64 string
    decoded_b64 = base64.b64decode(decoded_request)
    # convert byte string to string
    final = decoded_b64.decode("utf-8")
    return final

def encode_string(payload):
    # convert string to byte string
    decoded_request = payload
    bs = decoded_request.encode("utf-8")

    # encode byte string to base64
    encoded_b64 = base64.b64encode(bs)

    # add url encoding
    encoded_request = urllib.parse.quote(encoded_b64)
    return encoded_request

def main():
    if args.decode:
        print("Decoded string:\n")
        print(decode_string(args.payload))

    if args.encode:
        print("Encoded string:\n")
        print(encode_string(args.payload))

if __name__ == "__main__":
    main()
