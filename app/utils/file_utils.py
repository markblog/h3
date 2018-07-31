import os
import pandas as pd

def get_current_dir_files(path):
    if path:
        return [ path + '/' + f for f in os.listdir(path) if os.path.isfile(path + '/' + f) ]
    return None

def get_current_dir_first_file(path):
    if path:
        return [ path + '/' + f for f in os.listdir(path) if os.path.isfile(path + '/' + f) ][0]
    return None

def remove_file_extensions(path):
    if path:
        return os.path.splitext(path)[0].split('/')[-1]
    return None

def get_dataframe_from_csv(paths, encoding):
    if paths:
        return {remove_file_extensions(path):pd.read_csv(path, encoding =encoding,thousands=',') for path in paths}
    return None

def get_dataframes_from_excel(path, encoding):
    if path:
        ef = pd.ExcelFile(path)
        sheet_list = ef.sheet_names
        return {'_'.join(sheet.split()).lower(): ef.parse(sheet, thousands=',') for sheet in sheet_list}
    return None


