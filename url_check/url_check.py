import requests
import time
import datetime
from typing import List
from url_check.log import Log

# Units
class UrlCheckUnit:
    
    def __init__(self, url: str):
        self.url: str = ""
        if "http://" in url or "https://" in url:
            self.url = url
        else:
            self.url = "https://" + url
        self.status_codes: List[int] = []
        self.response_times: List[int] = []

# Check

class UrlCheck:

    def __init__(self, units: List[UrlCheckUnit], delay_sec: int):
        self.units = units
        self.delay_sec: int = delay_sec
        Log.info('')
        Log.info('*'*15)
        Log.info('Monitor urls:')
        for unit in self.units:
            Log.info('-', unit.url)
        Log.info('Every', delay_sec, 'seconds.')
        Log.info('*'*15)
        Log.info('')

    def run(self, verbose_logs: bool = False):
        while True:
            last: time = time.time()
            now: time = time.time()
            for unit in self.units:
                last = time.time()
                
                try:
                    response = requests.get(unit.url)
                except requests.exceptions.RequestException as exception:
                    now: datetime = datetime.datetime.now()
                    current_time: str = now.strftime("%H:%M:%S")
                    Log.error(current_time, exception)
                    continue
                
                now: time = time.time()
                # unit.status_codes.append(response.status_code)
                # unit.response_times.append(now-last)
                UrlCheck.print_response(unit.url, response, now-last, verbose=verbose_logs)

            time.sleep(self.delay_sec)
    
    @staticmethod
    def print_response(url: str, response, response_time: int, verbose: bool = False):
        now: datetime = datetime.datetime.now()
        current_time: str = now.strftime("%H:%M:%S")
        message: str = str(current_time) + ': ' + url + ' - ' + str(response.status_code) + ' - ' + str(response_time) + 'sec'
        if response.status_code == 200:
            if verbose:
                Log.happy(message)
        else:
            Log.error(message)
            Log.error(response.content)
