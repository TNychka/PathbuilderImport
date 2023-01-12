def stat_mapping(stat_str: str) -> int:
    if stat_str == "str":
        return 0
    elif stat_str == "dex":
        return 1
    elif stat_str == "con":
        return 2
    elif stat_str == "int":
        return 3
    elif stat_str == "wis":
        return 4
    elif stat_str == "cha":
        return 5

def size_mapping(size_str: str) -> int:
    if size_str == "med":
        return 2
    elif size_str == "sma":
        return 1
    else:
        raise IOError("Unknown size mapping " + size_str)