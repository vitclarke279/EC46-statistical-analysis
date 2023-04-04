def find_extreme_value(values_list: list, mode: str) -> str:
    """
    Finds the minimum or maximum value in a list.
    Args:
        values_list: A list of values.
        mode: A string that specifies whether to find the minimum or maximum value.
            Must be either 'min' or 'max'.
    Returns:
        The minimum or maximum value in the list, depending on the mode.
    """
    if mode == 'min':
        return min(values_list)
    elif mode == 'max':
        return max(values_list)
    else:
        raise ValueError('Mode must be "min" or "max"')
