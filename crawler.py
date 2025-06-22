import requests
from bs4 import BeautifulSoup
import re

# Your target URL (non-onion for now)
url = "http://[::1]:8000/"

# Optional: use Tor proxy for .onion sites later
use_tor = False
proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}

try:
    print(f"[*] Crawling: {url}")
    response = requests.get(url, proxies=proxies if use_tor else None, timeout=10)
    
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    print("\n--- Page Content (First 500 characters) ---")
    print(text[:500])  # Just show a snippet

    # Example: Find emails
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    if emails:
        print(f"\n[+] Found Emails: {emails}")
    else:
        print("[-] No emails found.")

    # Example: Find credentials (user:pass patterns)
    credentials = re.findall(r"[\w\.-]+:[\w\.-]+", text)
    if credentials:
        print(f"\n[+] Found Potential Credentials: {credentials}")
    else:
        print("[-] No credentials pattern found.")

except Exception as e:
    print(f"[!] Error: {e}")
