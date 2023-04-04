from csv import DictReader
from typing import List


def convert_csv_into_list_of_dicts(csv: str) -> List[dict]:
    """
    Reads a CSV file and converts its contents into a list of dictionaries.
    Args:
        csv (str): The path to the CSV file to be read.
    Returns:
        list: A list of dictionaries representing the rows in the CSV file.
    """
    with open(csv, mode='r') as csv_file:
        dict_reader = DictReader(csv_file)
        list_of_dicts = list(dict_reader)

    return list_of_dicts


def get_list_of_values(data_list: List[dict], value_key: str) -> list:
    """
    Using the given value key, create the list of values from the given list
    of dictionaries.
    Args:
        data_list (List(dict)): The list of dictionaries to parse.
        value_key (str): The value key used to extract data from given list of
        dictionaries.
    Returns:
        list: A list of values extracted from data_list using key_value.
    """
    return [
        data_dict[value_key] for data_dict in data_list if value_key in data_dict
    ]


def convert_values_in_list_to_specified_type(values_list: list, type: type) -> list:
    """
    Using the given value key, create the list of values from the given list
    of dictionaries.
    Args:
        values_list (list): The list of values to convert.
        type (str): The type to convert the values to.
    Returns:
        list: A list of values of given type.
    """
    return list(map(type, values_list))
