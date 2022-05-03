import argparse
import json
from typing import List
from url_check.url_check import UrlCheck, UrlCheckUnit

if __name__ == '__main__':
    # parse arguments
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='json encoded config',type=json.loads)

    args: parser = parser.parse_args()
    CONFIG: json.loads = args.config
    
    units: List[UrlCheckUnit] = []
    for url in CONFIG['urls']:
        units.append(UrlCheckUnit(url))

    url_check: UrlCheck = UrlCheck(units)
    url_check.run()

# python3 -m url_check --config '{"urls": ["https://example.com"]}'