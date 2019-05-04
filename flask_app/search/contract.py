import logging
import datetime
import json
import os
from elasticsearch_dsl import Search, Q
from elasticsearch import Elasticsearch


log = logging.getLogger(__name__)


class ContractQuery:
    def search(self, page, per_page, **kwargs):
        try:
            s = Search(
                using=Elasticsearch([os.getenv("ELASTICSEARCH_URL")]),
                index="bitjobboard",
                doc_type="contract",
            )
            log.debug(kwargs)
            if kwargs:
                queryargs = [
                    f"Q('multi_match',{kwkey}='{kwval}')"
                    for kwkey, kwval in kwargs.items()
                    if kwval is not None
                ]
                queryargs = " | ".join(queryargs)
                s = s.query(eval(queryargs))

            response = s[(page - 1) * per_page : per_page].execute()
            log.debug(self._formatted_query_response(response))
            return self._formatted_query_response(response)

        except Exception:
            logging.exception("Trouble querying")

    def _formatted_query_response(self, response):
        respdict = response.to_dict()
        print(respdict)
        formattedoutput = [hit["_source"] for hit in respdict["hits"]["hits"]]
        return formattedoutput
