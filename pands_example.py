"""
idea - create a class decorator to apply along with the dataframe editing functions;
      - 'titles' up the column names and removes the blank spaces that may occur;
"""
import pandas as pd
import functools


class FormatColumns:
    """
    decorator used to convert to Title the column names and remove blank spaces
    """
    def __init__(self, fnc):
        self.fnc = fnc
        functools.update_wrapper(self, fnc)

    def __call__(self, *args, **kwargs):
        try:
            out_df = pd.DataFrame(self.fnc(*args, **kwargs))
        except ValueError:
            return
        else:
            out_df.columns = [str(c_name).title().strip() for c_name in out_df.columns]
            return out_df



def format_colums(fnc):
    """
    same decorator as above but other mehtod - function;
    returns the same as FormatColumns
    """
    @functools.wraps(fnc)
    def wrapper(*args, **kwargs):
        try:
            out_df = pd.DataFrame(fnc(*args, **kwargs))
        except ValueError:
            return
        else:
            out_df.columns = [str(c_name).title().strip() for c_name in out_df.columns]
            return out_df
    return wrapper



@FormatColumns
def manipulate_df(x_df: pd.DataFrame) -> pd.DataFrame:
    """
    applies various changes to the initial df - e.g. adding new columns
    """

    x_df['Job'] = 'undefined'
    x_df['age_to_months'] = x_df['age'] * 12
    return x_df



dummy_df = pd.read_excel(r'data/dummy.xlsx')
man_df = manipulate_df(dummy_df)
print(man_df)  #  Name  Age   Location  Job  Age_To_Months


print(manipulate_df.__name__) # manipulated_df; without the functools.wraps/update_wrapper will return <wrapper>




