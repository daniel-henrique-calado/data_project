import glob
import os

# import openpyxl
from typing import List

import pandas as pd


def extract_from_excel(input_path: str) -> List[pd.DataFrame]:
    """
    function to read files from a folder "data/input" and return a dataframe lists

    args: input_path(str): folder path with all files

    return: dataframes lists
    """

    all_files = glob.glob(os.path.join(input_path, '*.xlsx'))
    df_list = []

    for file in all_files:
        df_list.append(pd.read_excel(file))

    return df_list


if __name__ == '__main__':
    path = 'data/input'
    data_frame_list = extract_from_excel(path)

    print(data_frame_list)
