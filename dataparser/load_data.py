import json
import logging
from pathlib import PosixPath

from django.conf import settings

BANK_MARKETING_FILE_PATH = settings.BASE_DIR.joinpath("data/bank-marketing.json")
ECOMMERCE_FILE_PATH = settings.BASE_DIR.joinpath("data/ecommerce.json")
log = logging.getLogger(__name__)


def parsing_multi_dimesions(x: list) -> list:
    return x['string'].split('&')


def flatten_list_uniques(z: list) -> list:
    return list(set([item for sublist in z for item in sublist]))


def parsing_single_dimesions(y: list) -> list:
    # isalpha handles all the other equalites <=, >=. etc
    return "".join([c for c in y.split("=")[0]if c.isalpha()])


def parse_file(file_name: PosixPath) -> list:
    dimesions = set()
    try:
        f = open(file_name)
        data = json.load(f)
        x1 = list(map(parsing_multi_dimesions, data))
        x2 = flatten_list_uniques(x1)
        dimesions = set(list(map(parsing_single_dimesions, x2)))
    except Exception as e:
        log.error(e)
    finally:
        return list(dimesions)
