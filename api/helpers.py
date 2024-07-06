def parse_list(data):
    """"
    The purpose of this function is to parse a list of data and return a string
    E.g. ["a", "b", "c"] => "a, b, c"
    If the list has only one item, it should return the item as a string
    """
    if len(data) > 1:
        return ", ".join(data)
    return data[0]