from CBLClient.Client import Client
from CBLClient.Args import Args
from keywords.utils import log_info


class Query:
    _client = None
    _baseUrl = None

    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

        # If no base url was specified, raise an exception
        if not self.baseUrl:
            raise Exception("No baseUrl specified")

        self._client = Client(baseUrl)

    ############
    # Collator #
    ############
    def query_collator_ascii(self, ignoreCase):
        args = Args()
        args.setString("ignoreCase", ignoreCase)

        return self._client.invokeMethod("query_collator_ascii", args)

    def query_collator_unicode(self, ignoreCase, ignoreAccents):
        args = Args()
        args.setString("ignoreCase", ignoreCase)
        args.setString("ignoreAccents", ignoreAccents)

        return self._client.invokeMethod("query_collator_unicode", args)

    def query_expression_property(self, prop):
        args = Args()
        args.setString("property", prop)

        return self._client.invokeMethod("query_expression_property", args)

    def query_datasource_database(self, database):
        args = Args()
        args.setString("database", database)

        return self._client.invokeMethod("query_datasource_database", args)

    def query_create(self, select_prop, from_prop, whr_key_prop, whr_val):
        args = Args()
        args.setString("select_prop", select_prop)
        args.setMemoryPointer("from_prop", from_prop)
        args.setString("whr_key_prop", whr_key_prop)
        args.setString("whr_val", whr_val)

        return self._client.invokeMethod("query_create", args)

    def query_run(self, query):
        args = Args()
        args.setString("query", query)

        return self._client.invokeMethod("query_run", args)

    def query_next_result(self, query_result_set):
        args = Args()
        args.setString("query_result_set", query_result_set)

        return self._client.invokeMethod("query_next_result", args)

    def query_result_string(self, query_result, key):
        args = Args()
        args.setString("query_result", query_result)
        args.setString("key", key)

        return self._client.invokeMethod("query_result_string", args)
