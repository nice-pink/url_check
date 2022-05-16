import argparse
import json
import sys
from typing import List
from url_check.url_check import UrlCheck, UrlCheckUnit
from url_check.log import Log

if __name__ == '__main__':
    # parse arguments
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='Json encoded config',type=json.loads)
    parser.add_argument('-i', '--interval', help='Repeat check every X seconds. Default: 60',type=int, default=60)
    parser.add_argument('-v', '--verbose', help='Print success logs. [True/False]',type=str, default='')

    args: parser = parser.parse_args()
    CONFIG: json.loads = args.config

    if not CONFIG:
        Log.error('Error: No config set.')
        sys.exit(1)

    INTERVAL: int = args.interval
    
    VERBOSE: str = args.verbose
    
    units: List[UrlCheckUnit] = []
    for url in CONFIG['urls']:
        units.append(UrlCheckUnit(url))
        
    verbose_logs: bool = False
    if VERBOSE.upper() == 'TRUE':
        verbose_logs = True

    url_check: UrlCheck = UrlCheck(units,delay_sec=INTERVAL)
    url_check.run(verbose_logs=verbose_logs)

# python3 -m url_check --config '{"urls": ["https://example.com"]}'
