import pandas as pd
from typing import List


def concat_data_frames(data_frame_list:List[pd.DataFrame]) -> pd.DataFrame:
    """
    function to transform a list of dataframes in a single dataframe

    args: List[pd.Dataframe]: list of dataframes

    return: dataframe
    """
    return pd.concat(data_frame_list, ignore_index=True)