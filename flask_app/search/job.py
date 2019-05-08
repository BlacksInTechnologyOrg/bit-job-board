import logging
import datetime
import json
import os
from elasticsearch_dsl import Search, Q, Mapping
from elasticsearch import Elasticsearch
from .searchutils import formatted_query_response

log = logging.getLogger(__name__)


class JobQuery:
    def search(self, page, per_page, **kwargs):
        try:
            s = Search(
                using=Elasticsearch([os.getenv("ELASTICSEARCH_URL")]), index="job"
            )
            log.debug(kwargs)
            print(
                Mapping.from_es(
                    index="job", using=Elasticsearch([os.getenv("ELASTICSEARCH_URL")])
                )
            )
            if kwargs:
                queryargs = [
                    f"Q('match',{kwkey}='{kwval}')"
                    for kwkey, kwval in kwargs.items()
                    if kwval is not None
                ]
                queryargs = " | ".join(queryargs)
                s = s.query(eval(queryargs))

            response = s[(page - 1) * per_page : per_page].execute()
            log.debug(formatted_query_response(response))
            return formatted_query_response(response)

        except Exception:
            logging.exception("Trouble querying")
