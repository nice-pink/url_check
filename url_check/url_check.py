import requests
import time
import datetime
from typing import List
from url_check.log import Log

# Units
class UrlCheckUnit:
    
    def __init__(self, url: str):
        self.url: str = url
        self.status_codes: List[int] = []
        self.response_times: List[int] = []

# Check

class UrlCheck:

    def __init__(self, units: List[UrlCheckUnit]):
        self.units = units
        Log.info('')
        Log.info('*'*15)
        Log.info('Monitor urls:')
        for unit in self.units:
            Log.info('-', unit.url)
        Log.info('*'*15)
        Log.info('')

    def run(self, delay_sec: int = 20, verbose_logs: bool = False):
        while True:
            last: time = time.time()
            now: time = time.time()
            for unit in self.units:
                last = time.time()
                
                try:
                    response = requests.get(unit.url)
                except requests.exceptions.RequestException as exception:
                    Log.error(exception)
                
                now: time = time.time()
                # unit.status_codes.append(response.status_code)
                # unit.response_times.append(now-last)
                UrlCheck.print_response(unit.url, response.status_code, now-last, verbose=verbose_logs)

            time.sleep(delay_sec)
    
    @staticmethod
    def print_response(url: str, status_code: int, response_time: int, verbose: bool = False):
        now: datetime = datetime.datetime.now()
        current_time: str = now.strftime("%H:%M:%S")
        message: str = str(current_time) + ': ' + url + ' - ' + str(status_code) + ' - ' + str(response_time) + 'sec'
        if status_code == 200:
            if verbose:
                Log.happy(message)
        else:
            Log.error(message)
