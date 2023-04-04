from statistics import mean, median

import utils.read_data as data_utils
import utils.statistics as statistic_utils

csv_file = "csv_files/uk_ec46_tt.csv"

list_of_dicts = data_utils.convert_csv_into_list_of_dicts(csv=csv_file)

temperature_list = data_utils.get_list_of_values(
    data_list=list_of_dicts, value_key='awg_areacalc_val'
)
temperature_list = data_utils.convert_values_in_list_to_specified_type(
    values_list=temperature_list, type=float
)

lowest_temperature = statistic_utils.find_extreme_value(
    values_list=temperature_list, mode='min'
)
time_of_lowest_temperature = list_of_dicts[lowest_temperature[1]]['awg_areacalc_forecast_dtg']

print('*****FORECAST*****')
print(f'Minimum forecasted temperature is {lowest_temperature[0]} degrees')
print(f'This temperature is forecasted to be at {time_of_lowest_temperature}')
print('------')

highest_temperature = statistic_utils.find_extreme_value(
    values_list=temperature_list, mode='max'
)
time_of_highest_temperature = list_of_dicts[highest_temperature[1]]['awg_areacalc_forecast_dtg']

print(f'Maximum forecasted temperature is {highest_temperature[0]} degrees')
print(f'This temperature is forecasted to be at {time_of_highest_temperature}')
print('------')

print(f'{mean(temperature_list)} is the mean temperature of the forecast.')
print('------')
print(f'{median(temperature_list)} is the median temperature of the forecast.')
print('------')
