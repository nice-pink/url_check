import argparse
import json
from typing import List
from url_check.url_check import UrlCheck, UrlCheckUnit

if __name__ == '__main__':
    # parse arguments
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='Json encoded config',type=json.loads)
    parser.add_argument('-v', '--verbose', help='Print success logs. [True/False]',type=str, default='')

    args: parser = parser.parse_args()
    CONFIG: json.loads = args.config
    VERBOSE: str = args.verbose
    
    units: List[UrlCheckUnit] = []
    for url in CONFIG['urls']:
        units.append(UrlCheckUnit(url))
        
    verbose_logs: bool = False
    if VERBOSE.upper() == 'TRUE':
        verbose_logs = True

    url_check: UrlCheck = UrlCheck(units)
    url_check.run(verbose_logs=verbose_logs)

# python3 -m url_check --config '{"urls": ["https://example.com"]}'
