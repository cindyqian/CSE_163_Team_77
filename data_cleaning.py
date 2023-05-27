"""
Name: Sarah Khan, Cindy Qian, and Junhee Park
Group: P077
Implement functions that perform data cleaning by getting
the percentage of unique words, isolation, economic stress,
substance use, domestic stress, and suicidality from a dataset.
It also implements a function that combines a list of dataframes
into a new dataframe.
"""

import pandas as pd

def _get_percentage(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Given a column name and data, computes the percentage of the
    words of the given column name related out of
    all words for each Reddit post.
    Returns a 2 column DataFrame with the rows
    representing each Reddit post, the first column being
    the post, and the second column being the percentage.
    Use the columns passed-in and n_words to calculate
    the percentage.
    Assumes column_name is found in the dataset.
    """
    df = pd.DataFrame()
    df['post'] = data['post']
    df['date'] = data['date']
    df['percentage'] = data[column_name] / data['n_words'] * 100.0
    df['type_of_word'] = column_name
    # df = df.reset_index()
    # df = df.rename(columns={'index' : 'index_' + column_name}) # Rename the index column
    # df = df.set_index('index_' + column_name)  # Set the index column as the new index
    # df["unique_id"] = data[column_name] + data['index_' + column_name]
    return df


def get_unique_word_percentage(data: pd.DataFrame) -> pd.DataFrame:
    """
    Takes the data and computes the percentage of unique
    words related out of all words for each Reddit post.
    It should return a 2 column DataFrame with the rows
    representing each Reddit post, the first column being
    the post, and the second column being the percentage.
    Use the columns n_unique_words and n_words to calculate
    the percentage.
    """
    return _get_percentage(data, 'n_unique_words')

def get_isolation_percentage(data: pd.DataFrame) -> pd.DataFrame:
    """
    Takes the data and computes the percentage of words related
    to 'isolation' out of all words for each Reddit post. It should
    return a 2 column DataFrame with the rows representing each
    Reddit post, the first column being the post, and the second
    column being the percentage. Use the columns isolation_total
    and n_words to calculate the percentage.
    """
    return _get_percentage(data, 'isolation_total')

def get_economic_stress_percentage(data: pd.DataFrame) -> pd.DataFrame:
    """
    Takes the data and computes the percentage of words related
    to 'economic stress' out of all words for each Reddit post. It should
    return a 2 column DataFrame with the rows representing each
    Reddit post, the first column being the post, and the second
    column being the percentage. Use the columns economic_stress_total
    and n_words to calculate the percentage.
    """
    return _get_percentage(data, 'economic_stress_total')

def get_substance_use_percentage(data: pd.DataFrame) -> pd.DataFrame:
    """
    Takes the data and computes the percentage of words related
    to 'substance use' out of all words for each Reddit post. It should
    return a 2 column DataFrame with the rows representing each
    Reddit post, the first column being the post, and the second
    column being the percentage. Use the columns substance_use_total
    and n_words to calculate the percentage.
    """
    return _get_percentage(data, 'substance_use_total')

def get_domestic_stress_percentage(data: pd.DataFrame) -> pd.DataFrame:
    """
    Takes the data and computes the percentage of words related
    to 'domestic stress' out of all words for each Reddit post. It should
    return a 2 column DataFrame with the rows representing each
    Reddit post, the first column being the post, and the second
    column being the percentage. Use the columns domestic_stress_total
    and n_words to calculate the percentage.
    """
    return _get_percentage(data, 'domestic_stress_total')


def get_suicidality_percentage(data: pd.DataFrame) -> pd.DataFrame:
    """
    Takes the data and computes the percentage of words related
    to 'suicidality' out of all words for each Reddit post. It should
    return a 2 column DataFrame with the rows representing each
    Reddit post, the first column being the post, and the second
    column being the percentage. Use the columns suicidality_total
    and n_words to calculate the percentage.
    """
    return _get_percentage(data, 'suicidality_total')

def combine_dataframes(data: list[pd.DataFrame]) -> pd.DataFrame:
    """
    Given a list of DataFrames, combine_dataframes returns a new
    Dataframe with the columns combined.
    """
    # concatenated = pd.concat(data, ignore_index=True)
    # concatenated = concatenated.reset_index(drop=True)
    concatenated = pd.concat(data)
    concatenated = concatenated.sort_values(by=['post'])
    # for df in data[1:]:
    #     # combined_data = combined_data.join(df)
    #     # combined_data = combined_data.merge(df, left_on="post", right_on="post", how="outer")
    #     # combined_data = combined_data.merge(df, left_on="unique_id", right_on="unique_id", how="outer")
    #     combined_data.concat(df)
    return concatenated
