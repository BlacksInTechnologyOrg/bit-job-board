settings = {
    "settings": {
        "analysis": {
            "filter": {
                "ngram_filter": {"type": "ngram", "min_gram": 2, "max_gram": 20}
            },
            "analyzer": {
                "ngram_analyzer": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "ngram_filter"],
                }
            },
        }
    },
    "mappings": {
        "doc": {
            "properties": {
                "description": {
                    "type": "text",
                    "term_vector": "yes",
                    "analyzer": "ngram_analyzer",
                    "search_analyzer": "standard",
                },
                "title": {"type": "text", "term_vector": "yes"},
            }
        }
    },
}
