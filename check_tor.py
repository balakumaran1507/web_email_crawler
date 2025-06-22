import requests

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

try:
    r = requests.get("http://check.torproject.org", proxies=proxies, timeout=20)
    if "Congratulations" in r.text:
        print("[✓] TOR connection working!")
    else:
        print("[x] Connected, but not through Tor.")
except Exception as e:
    print("[-] Error:", e)
