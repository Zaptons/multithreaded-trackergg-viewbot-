import os, requests, random, concurrent.futures
from threading import Lock
from user_agent import generate_user_agent
from src.modules.utils.logger import Logger
from src.modules.helper.config import Config
from concurrent.futures import ThreadPoolExecutor
from curl_cffi import requests

class ViewBot():
    def __init__(self):
        self.views_sent, self.views_ratelimited, self.views_failed = 0, 0, 0
        self.config = Config()
        self.logger = Logger()

    # Proxy scraper
    def load_proxy_list(self):
        with open(self.config.proxies_file, "r", encoding="utf8", errors="ignore") as file:
            self.proxy_list = file.read().splitlines()
        return self.proxy_list

    # Set a proxy each request
    def set_proxy(self):
        proxy = random.choice(self.proxy_list)
        return {'http': f"http://{proxy}", 'https': f'http://{proxy}'}
    
    def send_request(self):
        while True:
            session = requests.Session()
            session.proxies = self.set_proxy()
            user_agent = generate_user_agent()

            # Set title
            if os.name == 'nt':
                os.system(f"title Tracker.gg View Bot • Views sent: {self.views_sent} • Views failed: {self.views_failed} • Views rate limited: {self.views_ratelimited}• Profile: {self.config.link_to_boost}")

            headers = {
                'Accept': 'application/json,text/plain, */*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.6',
                'Host' : 'api.tracker.gg',
                'Origin' : 'https://tracker.gg',
                'Referer' : 'https://tracker.gg/',
                'sec-ch-ua' : '"Google Chrome";v="125","Chromium";v="125","Not.A/Brand";v="25"',
                'sec-ch-ua-mobile' : '?0',
                'sec-ch-ua-platform' : '"Windows"',
                'Sec-Fetch-Dest' : 'empty',
                'Sec-Fetch-Mode' : 'cors',
                'Sec-Fetch-Site' : 'same-site',
                "User-Agent": user_agent,
            }

            response = session.get(self.config.link_to_boost, headers=headers, impersonate="chrome101")

            if response.status_code == 429:
                self.logger.log("ERROR", "You are being rate limited, retrying.")
                self.views_ratelimited += 1
                return False

            if response.status_code != 200:
                self.logger.log("ERROR", f"Error sending request: {response.status_code}")
                self.views_failed += 1
                return False
            
            self.views_sent += 1
            self.logger.log("SUCCESS", f"Successfully sent request. Total views sent: {self.views_sent}")
            return True
    
    def start(self):
        # Load proxies from file
        self.logger.log("INFO", "Loading proxies...")
        self.load_proxy_list()

        # Start the view bot
        self.logger.log("INFO", "Starting view bot threads...")
        with ThreadPoolExecutor(max_workers=self.config.threads) as executor:
            while True:
                futures = {executor.submit(self.send_request) for _ in range(self.config.threads)}
                concurrent.futures.wait(futures)
