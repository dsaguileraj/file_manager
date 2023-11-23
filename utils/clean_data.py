

class CleanData:

    @staticmethod
    def clean_filters(filters):
        c_filters = {}
        bool_mappings = {"true": True, "false": False}
        for k, v in filters.items():
            if isinstance(v, str) and v.lower() in bool_mappings:
                c_filters[k] = bool_mappings[v.lower()]
            else:
                c_filters[k] = v
        return c_filters
