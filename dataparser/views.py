import logging

from django.conf import settings
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from dataparser.load_data import parse_file

log = logging.getLogger(__name__)


datafiles = {"BANK-MARKETING": settings.BASE_DIR.joinpath("data/bank-marketing.json"),
             "ECOMMERCE": settings.BASE_DIR.joinpath("data/ecommerce.json")}


# Create your views here.
class DimensionListView(GenericAPIView):
    def get_queryset(self):
        return None

    def get(self, request, **kwargs):
        try:
            file_name = kwargs["filename"]
            print(file_name)
            if file_name.upper() in datafiles.keys():
                return Response(data=parse_file(datafiles[file_name.upper()]), status=status.HTTP_200_OK)
            else:
                return Response(data={"error": "filename must be either bank_marketing or ecommerce"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            log.error(e)
            return Response(data={"error": "Server on break"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
