from django.conf import settings
import logging
log = logging.getLogger(__name__)


DATAFILE = {"BANK-MARKETING": settings.BASE_DIR.joinpath("data/bank-marketing.json"),
            "ECOMMERCE": settings.BASE_DIR.joinpath("data/ecommerce.json")}
PARSED_DATAFILE = {"BANK-MARKETING": settings.BASE_DIR.joinpath("data/parsed-bank.json"),
                   "ECOMMERCE": settings.BASE_DIR.joinpath("data/parsed-ecommerce.json")}

IMPACT_VARIABLE = {"BANK-MARKETING": "avg_duration_impact",
                   "ECOMMERCE": "ItemTotalPrice_impact"
                   }
