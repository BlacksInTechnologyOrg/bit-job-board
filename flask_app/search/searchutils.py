def formatted_query_response(response):
    respdict = response.to_dict()
    print(respdict)
    formattedoutput = [hit["_source"] for hit in respdict["hits"]["hits"]]
    return formattedoutput
