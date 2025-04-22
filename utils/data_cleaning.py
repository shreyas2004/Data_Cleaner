import pandas as pd

def clean_data(data):
    duplicates = data[data.duplicated()]
    data = data.drop_duplicates()

    for col in data.columns:
        if data[col].dtype in ['float64', 'int64']:
            data[col].fillna(data[col].mean(), inplace=True)
        else:
            data.dropna(subset=[col], inplace=True)

    return data, duplicates
