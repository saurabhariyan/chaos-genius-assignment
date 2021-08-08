import json
from dataparser.consts import log
from pathlib import PosixPath


def parsing_multi_dimesions(x: list) -> list:
    return x['string'].split('&')


def flatten_list_uniques(z: list) -> list:
    return list(set([item for sublist in z for item in sublist]))


def parsing_single_dimesions(y: list) -> list:
    # isalpha handles all the other equalites <=, >=. etc
    return "".join([c for c in y.split("=")[0]if c.isalpha()])


def get_dimensions(file_name: PosixPath) -> list:
    dimesions = set()
    try:
        f = open(file_name)
        data = json.load(f)
        x1 = list(map(parsing_multi_dimesions, data))
        # flattening lists of list into list and parsing on only uniques to reduce complexity
        x2 = flatten_list_uniques(x1)
        dimesions = set(list(map(parsing_single_dimesions, x2)))

    except Exception as e:
        log.error(e)
    finally:
        return list(dimesions)


def parse_datafile(file_name: PosixPath) -> list:
    """
    Appends a parent dict to each node of type {dimension:parent-id}.
    x is a parent of y if :
        - intersection of dimension values of x and y is not null
        - AND x has fewer dimensions than y

    - make a parent_map of all the seen dimensions and their node id
    - if the new dimension is not in parent map: parent of node for that dimension is -1

    Side Effect: needs to add id to the given data. can be uuid, used counter here for simplictiy.
    """
    data = json.load(open(file_name))
    count = 0
    parent_map = {}
    sorted_data = sorted(data, key=lambda x: len(x['string'].split('&')))
    for node in sorted_data:
        node_dimensions = node['string'].split('&')  # handles multiple dimensions
        node['parent'] = {}
        count += 1
        for node_dimension in node_dimensions:
            node_dimension = node_dimension.strip()
            node['id'] = count
            key = "".join([c for c in node_dimension.split("=")[0]if c.isalpha()])  # eg:
            parent_dimension_id = parent_map.get(node_dimension)
            if parent_dimension_id:
                node['parent'][key] = parent_dimension_id
            else:
                parent_map[node_dimension] = count
                node['parent'][key] = -1

    return data


def dump_json_file(data: list, file_name: PosixPath, append=False):
    json_object = json.dumps(data, indent=2, sort_keys=True)
    with open(file_name, "w") as dumpfile:
        dumpfile.write(json_object)
