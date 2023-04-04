from csv import DictReader
from typing import List


def convert_csv_into_list_of_dicts(csv) -> List[dict]:
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
