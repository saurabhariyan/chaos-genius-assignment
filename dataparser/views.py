import logging

from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response

from dataparser.load_data import parse_file

log = logging.getLogger(__name__)


datafiles = {"BANK_MARKETING": settings.BASE_DIR.joinpath("data/bank-marketing.json"),
             "ECOMMERCE": settings.BASE_DIR.joinpath("data/ecommerce.json")}


# Create your views here.
class DimensionListView(generics.ListAPIView):
    def list(self):
        try:
            file_name = self.kwargs["filename"]
            if file_name.upper() in ("BANK_MARKETING", "ECOMMERCE"):
                return Response(data=parse_file(datafiles[file_name.upper()]), status=status.HTTP_200_OK)
            else:
                return Response(data={"error": "filename must be either bank_marketing or ecommerce"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            log.error(e)
            return Response(data={"error": "Server on break"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
