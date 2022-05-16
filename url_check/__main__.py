import argparse
import json
import sys
from typing import List
from url_check.url_check import UrlCheck, UrlCheckUnit
from url_check.log import Log

if __name__ == '__main__':
    # parse arguments
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='json encoded config',type=json.loads)

    args: parser = parser.parse_args()
    CONFIG: json.loads = args.config

    if not CONFIG:
        Log.error('Error: No config set.')
        sys.exit(1)
    
    units: List[UrlCheckUnit] = []
    for url in CONFIG['urls']:
        units.append(UrlCheckUnit(url))

    url_check: UrlCheck = UrlCheck(units)
    url_check.run()

# python3 -m url_check --config '{"urls": ["https://example.com"]}'