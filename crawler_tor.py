import requests
from bs4 import BeautifulSoup
import re

url = "http://r35n4jqb6bng3nb2bu7fhgojv5kecilxme3szvh46lyewboncxgki3qd.onion/"

# Configure Tor SOCKS5 proxy
proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

print(f"[•] Connecting to: {url}")
try:
    res = requests.get(url, proxies=proxies, headers=headers, timeout=30)
    res.raise_for_status()
    print("[+] Connection successful via Tor.")
except Exception as e:
    print("[-] Failed to connect:", e)
    exit()

soup = BeautifulSoup(res.text, "html.parser")
text = soup.get_text()

# --- Extract Data ---
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
credentials = re.findall(r"\b[a-zA-Z0-9_.+-]+:[a-zA-Z0-9_.!@#$%^&*+-]+\b", text)
ip_addresses = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)
onion_links = re.findall(r"http[s]?://[a-z2-7]{16,56}\.onion", text)

# --- Output ---
def print_list(title, data):
    print(f"\n== {title} ==")
    if data:
        for d in data:
            print("•", d)
    else:
        print("None found.")

print_list("Emails Found", emails)
print_list("Credentials Found", credentials)
print_list("IP Addresses Found", ip_addresses)
print_list(".onion Links Found", onion_links)

# Save to file
with open("crawl_output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("\n[✓] Full raw text saved to crawl_output.txt")
