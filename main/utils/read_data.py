from csv import DictReader
from datetime import datetime
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


def return_values_of_specific_week_days(values_list: list, days_of_week: list) -> list:
    """
    Processes the given list of values to return only the data of a specific week day.
    Args:
        values_list (list): The list of values to process.
        days_of_week (list): The week days to extract.
    Returns:
        list: A list of data only from the specified week_day.
    """
    filtered_data = []
    for value in values_list:
        date_time = datetime.strptime(value['awg_areacalc_forecast_dtg'], '%Y-%m-%d %H:%M:%S')
        day_of_week = date_time.strftime('%A')

        if day_of_week in days_of_week:
            filtered_data.append(value)

    return filtered_data
