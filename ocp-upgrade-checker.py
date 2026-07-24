#!/usr/bin/env python3
import urllib.request
import json
import ssl

def query_api(ocp_version, channel_name):

    default_cert_ca = '/etc/ssl/cert.pem'
    url = "https://api.openshift.com/api/upgrades_info/v1/graph?channel=" + channel_name

    # Create a standard client context
    #ssl_context = ssl.create_default_context()

    # Explicitly tell Python to load the OS default CA certificates
    #ssl_context.load_default_certs()
    #capath = ssl.get_default_verify_paths().openssl_cafile
    #print(capath)
    #ssl_context = ssl.create_default_context(cafile=capath)
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.load_verify_locations(default_cert_ca)

    # Create a request object (optional: add headers like User-Agent)
    req = urllib.request.Request(
        url, 
        headers={"Accept": "application/json"}
    )

    # Open the URL as a context manager to ensure clean closure
    with urllib.request.urlopen(req, context=ssl_context) as response:
        # 1. Read bytes from response
        # 2. Decode bytes to utf-8 string
        # 3. Parse JSON string to Python dict
        raw_data = response.read().decode("utf-8")
        data = json.loads(raw_data)
        
        print("Status Code:", response.status)
        print("Data:", data)


def main():
    query_api("4.20.15", "stable-4.21")


if __name__ == '__main__':
    main()
