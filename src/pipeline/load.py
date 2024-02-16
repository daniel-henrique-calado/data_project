import pandas as pd
import os

def load_excel(data_frame: pd.DataFrame, output_path:str, file_name:str) -> str:
    """
    Receives dataframes and create a excel file on desire path.

    args: 
        data_frame(pd.Dataframe): dataframe to be saved on a excel file format
        output_path(str): path to create the file
        file_name(str): file name to be created

    return: "Filed saved with sucess!"
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Filed saved with sucess!"