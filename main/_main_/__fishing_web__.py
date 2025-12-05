# ---Creator: t.me/GKSVGK ---Channel: t.me/iTechZIR,t.me/dev_2yt_code_c
#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import os
import concurrent.futures
import time

useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
headers = {"User-Agent": useragent}

def _current_time():
    return time.strftime('%H:%M:%S')

def _slow(text):
     print(text)

def _censored(text):
    pass

def _error_module(e):
    print(f"-  error importing modules: {e}")
    exit()

def _error_url():
    print("-  error: could not fetch the url Check the link or your connection")
    exit()

def _error(e):
    print(f"-  an error occurred: {e}")
    exit()

def _continue():
    input("\n-  end procees, please click")

def _run_phishing():
    print("""
╔══════════════════════════════════════════════════════╗
║                     PishingWeb                       ║
║               Pishing Page In Website                ║
║                                                      ║
║            Version: 1.0    Creator: 2yt              ║
╚══════════════════════════════════════════════════════╝
""")
    print(f"[{_current_time()}] -  selected user-agent: {useragent}")

    websiteurl = input(f"[{_current_time()}] - please enter the url: ").strip()
    if not websiteurl.startswith(("http://", "https://")):
        websiteurl = "https://" + websiteurl

    def _css_and_js(htmlcontent, baseurl):
        soup = BeautifulSoup(htmlcontent, 'html.parser')

        print(f"[{_current_time()}] - recovering css...")
        csslinks = soup.find_all('link', rel='stylesheet')
        allcss = []
        cssurls = [urljoin(baseurl, link['href']) for link in csslinks]
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            cssresponses = list(executor.map(lambda url: requests.get(url, headers=headers, timeout=5), cssurls))
            for cssresponse in cssresponses:
                if cssresponse.status_code == 200:
                    allcss.append(cssresponse.text)
                else:
                    print(f"[{_current_time()}] - error retrieving css from {cssresponse.url}")

        if allcss:
            styletag = soup.new_tag('style')
            styletag.string = "\n".join(allcss)
            soup.head.append(styletag)
            for link in csslinks:
                link.decompose()

        print(f"[{_current_time()}] - recovering javascript...")
        scriptlinks = soup.find_all('script', src=True)
        alljs = []
        jsurls = [urljoin(baseurl, script['src']) for script in scriptlinks]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            jsresponses = list(executor.map(lambda url: requests.get(url, headers=headers, timeout=5), jsurls))
            for jsresponse in jsresponses:
                if jsresponse.status_code == 200:
                    alljs.append(jsresponse.text)
                else:
                    print(f"[{_current_time()}] [+] - Error retrieving JS from {jsresponse.url}")

        if alljs:
            script_tag = soup.new_tag('script')
            script_tag.string = "\n".join(alljs)
            soup.body.append(script_tag)
            for script in scriptlinks:
                script.decompose()

        return soup.prettify()

    print(f"[{_current_time()}] - fetching html...")
    try:
        session = requests.Session()
        response = session.get(websiteurl, headers=headers, timeout=10)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            filename = re.sub(r'[\\/:*?"<>|]', '-', soup.title.string if soup.title else '__phishing_page__')

            outputdir = os.path.join("__fishing_list__")
            os.makedirs(outputdir, exist_ok=True)

            filehtml = os.path.join(outputdir, f"{filename}.html")
            finalhtml = _css_and_js(html_content, websiteurl)

            with open(filehtml, 'w', encoding='utf-8') as file:
                file.write(finalhtml)
            print(f"[{_current_time()}] [+] - Success ! Phishing page saved to: {filehtml}")
            _continue()
            
        else:
            _error_url()
    except Exception as e:
        _error(e)

if __name__ == "__main__":
    _run_phishing()


