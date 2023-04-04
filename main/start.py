from utils.read_data import convert_csv_into_list_of_dicts, get_list_of_values

csv_file = "csv_files/uk_ec46_tt.csv"

list_of_dicts = convert_csv_into_list_of_dicts(csv=csv_file)

awg_areacalc_val_list = get_list_of_values(
    data_list=list_of_dicts, value_key='awg_areacalc_val'
)
print(awg_areacalc_val_list)
