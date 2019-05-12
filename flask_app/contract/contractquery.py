import logging
import os
from elasticsearch_dsl import Search
from elasticsearch import Elasticsearch
from ..searchutils import formatted_query_response


log = logging.getLogger(__name__)


class ContractQuery:
    def search(self, page, per_page, **kwargs):
        try:
            s = Search(
                using=Elasticsearch([os.getenv("ELASTICSEARCH_URL")]), index="contract"
            )
            log.debug(kwargs)
            if kwargs:
                queryargs = [
                    f"Q('match',{kwkey}='{kwval}')"
                    for kwkey, kwval in kwargs.items()
                    if kwval is not None
                ]
                queryargs = " | ".join(queryargs)
                print(queryargs)
                s = s.query(eval(queryargs))

            response = s[(page - 1) * per_page : per_page].execute()
            log.debug(formatted_query_response(response))
            return formatted_query_response(response)

        except Exception:
            logging.exception("Trouble querying")
