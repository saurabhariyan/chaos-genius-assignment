
import json
from django.conf import settings
from pathlib import PosixPath

BANK_MARKETING_FILE_PATH = settings.BASE_DIR.joinpath("data/bank-marketing.json")
ECOMMERCE_FILE_PATH = settings.BASE_DIR.joinpath("data/ecommerce.json")


def parsing_multi_dimesions(x: list) -> list:
    return x['string'].split('&')


def flatten_list_uniques(z: list) -> list:
    return list(set([item for sublist in z for item in sublist]))


def parsing_single_dimesions(y: list) -> list:
    return "".join([c for c in y.split("=")[0]if c.isalpha()])


def parse_file(file_name: PosixPath) -> list:
    dimesions = set()
    f = open(file_name)
    data = json.load(f)
    x1 = list(map(parsing_multi_dimesions, data))
    x2 = flatten_list_uniques(x1)
    dimesions = set(list(map(parsing_single_dimesions, x2)))
    return list(dimesions)
