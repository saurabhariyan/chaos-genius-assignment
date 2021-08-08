import json
import os

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from dataparser.consts import DATAFILE, PARSED_DATAFILE, IMPACT_VARIABLE, log
from dataparser.load_data import dump_json_file, get_dimensions, parse_datafile


class DimensionListView(GenericAPIView):
    def get_queryset(self):
        return None

    def get(self, request, **kwargs):
        try:
            file_name = kwargs["filename"]
            if file_name.upper() in DATAFILE.keys():
                return Response(data=get_dimensions(DATAFILE[file_name.upper()]), status=status.HTTP_200_OK)
            else:
                return Response(data={"error": "filename must be either bank-marketing or ecommerce"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            log.error(e)
            return Response(data={"error": "Server on break"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TreeListView(GenericAPIView):

    def get_queryset(self):
        pass

    def get(self, request, **kwargs):
        try:
            file_name = kwargs.get("dataset").upper() or "BANK-MARKETING"
            node = kwargs.get("node").lower()

            if file_name.upper() not in DATAFILE.keys():
                return Response(data={"error": "data set must be either bank-marketing or ecommerce"}, status=status.HTTP_400_BAD_REQUEST)
            if node not in get_dimensions(DATAFILE[file_name]):
                return Response(data={"error": "invalid node"}, status=status.HTTP_400_BAD_REQUEST)
            try:
                min_impact = float(request.GET.get("min-impact", 0.00))
                levels = int(request.GET.get("levels", 3))
            except ValueError:
                return Response(data={"error": "impact and levels must be floatable"}, status=status.HTTP_400_BAD_REQUEST)

            if levels not in (2, 3):
                return Response(data={"error": "level must be either 2 or 3"}, status=status.HTTP_400_BAD_REQUEST)

            output_file_path = PARSED_DATAFILE[file_name]
            if os.path.isfile(output_file_path):
                data = json.load(open(output_file_path))
            else:
                data = parse_datafile(DATAFILE[file_name])
                dump_json_file(data, output_file_path)
            impact = IMPACT_VARIABLE[file_name]
            tree_data = list(filter(lambda x: x["parent"].get(node, False), data))
            pruned_tree_data = list(filter(lambda x: x[impact] > min_impact, tree_data))
            return Response(data=pruned_tree_data, status=status.HTTP_200_OK)
        except Exception as e:
            log.error(e)
            return Response(data={"error": "Server on break"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
