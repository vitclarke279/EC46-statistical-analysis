def find_extreme_value(values_list: list, mode: str) -> tuple:
    """
    Finds the minimum or maximum value in a list, along with its index.
    Args:
        values_list: A list of values.
        mode: A string that specifies whether to find the minimum or maximum value.
            Must be either 'min' or 'max'.
    Returns:
        The minimum or maximum value in the list, depending on the mode.
    """
    if mode == 'min':
        extreme_value = min(values_list)
        index = values_list.index(extreme_value)
    elif mode == 'max':
        extreme_value = max(values_list)
        index = values_list.index(extreme_value)
    else:
        raise ValueError('Mode must be "min" or "max"')
    return extreme_value, index
