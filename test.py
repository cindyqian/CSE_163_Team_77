"""
Name: Sarah Khan, Cindy Qian, and Junhee Park
Group: P077
This file tests functions that are implemented by data_cleaning.py
"""

import pandas as pd
import data_cleaning
from cse163_utils import assert_equals

TEST_FILE : str = 'test_features.csv'
TEST_PANDAS : pd.DataFrame = pd.read_csv(TEST_FILE)
FIRST_POST: str = 'Heroin Should I tell my ex wife that I tried heroin?'
SECOND_POST: str = 'I\'m scared Recently, I\'ve been getting deeper and deeper into my addiction with cocaine. I just ran out of what I had tonight and I\'m not able to get any till Thursday. As much as I don\'t want to get anymore, I feel like the urge just overpowers all logical reasoning. I\'m scared what will happen in the next few days. I\'ve been diagnosed with MDD and anxiety for almost 10 years and I know the next few days are probably going to be the worst. Not many people know what\'s going on and the ones that do, don\'t know how bad it has actually become. It also doesn\'t help that my roommate/friend has been high out of his mind on benzos and becomes verbally/emotionally abusive. I don\'t know what to do.'
THIRD_POST: str = 'How to deal with the emptiness of your addiction? I have to be clean for a few months but everytime I am I feel empty and hollow. I am a shopping addict so I guess some would say it isn\'t that bad but still, I want to save money.'
POST_LIST: list[str] = [FIRST_POST, SECOND_POST, THIRD_POST]

FIRST_DATE: str = '2019/04/16'
SECOND_DATE: str = '2019/04/16'
THIRD_DATE: str = '2019/08/13'
DATE_LIST: list[str] = [FIRST_DATE, SECOND_DATE, THIRD_DATE]


def test_get_unique_word_percentage() -> None:
    """
    Tests data_cleaning.py's get_unique_word_percentage().
    """
    expected_data = {'post': POST_LIST,
                     'date': DATE_LIST, 
                    'percentage': [81.8181818182, 59.7222222222, 80],
                    'type_of_word': ['n_unique_words', 'n_unique_words', 'n_unique_words']}
    expected_result = pd.DataFrame(data=expected_data)
    actual_result = data_cleaning.get_unique_word_percentage(TEST_PANDAS)
    assert_equals(expected_result, actual_result)


def test_get_isolation_percentage() -> None:
    """
    Tests data_cleaning.py's get_isolation_percentage().
    """
    expected_data = {'post': POST_LIST,
                     'date': DATE_LIST, 
                    'percentage': [0.0, 0.0, 2.0],
                    'type_of_word': ['isolation_total', 'isolation_total', 'isolation_total']}
    expected_result = pd.DataFrame(data=expected_data)
    actual_result = data_cleaning.get_isolation_percentage(TEST_PANDAS)
    assert_equals(expected_result, actual_result)


def test_get_economic_stress_percentage() -> None:
    """
    Tests data_cleaning.py's get_economic_stress_percentage().
    """
    expected_data = {'post': POST_LIST,
                     'date': DATE_LIST, 
                    'percentage': [0.0, 0.69444444444, 0.0],
                    'type_of_word': ['economic_stress_total', 'economic_stress_total', 'economic_stress_total']}
    expected_result = pd.DataFrame(data=expected_data)
    actual_result = data_cleaning.get_economic_stress_percentage(TEST_PANDAS)
    assert_equals(expected_result, actual_result)


def test_get_substance_use_percentage() -> None:
    """
    Tests data_cleaning.py's get_substance_use_percentage().
    """
    expected_data = {'post': POST_LIST,
                     'date': DATE_LIST, 
                    'percentage': [0.0, 0.69444444444, 0.0],
                    'type_of_word': ['substance_use_total', 'substance_use_total', 'substance_use_total']}
    expected_result = pd.DataFrame(data=expected_data)
    actual_result = data_cleaning.get_substance_use_percentage(TEST_PANDAS)
    assert_equals(expected_result, actual_result)


def test_get_domestic_stress_percentage() -> None:
    """
    Tests data_cleaning.py's get_domestic_stress_percentage().
    """
    expected_data = {'post': POST_LIST,
                     'date': DATE_LIST, 
                    'percentage': [0.0, 0.0, 0.0],
                    'type_of_word': ['domestic_stress_total', 'domestic_stress_total', 'domestic_stress_total']}
    expected_result = pd.DataFrame(data=expected_data)
    actual_result = data_cleaning.get_domestic_stress_percentage(TEST_PANDAS)
    assert_equals(expected_result, actual_result)


def test_get_suicidality_percentage() -> None:
    """
    Tests data_cleaning.py's get_suicidality_percentage().
    """
    expected_data = {'post': POST_LIST,
                     'date': DATE_LIST, 
                    'percentage': [0.0, 0.0, 2.0],
                    'type_of_word': ['suicidality_total', 'suicidality_total', 'suicidality_total']}
    expected_result = pd.DataFrame(data=expected_data)
    actual_result = data_cleaning.get_suicidality_percentage(TEST_PANDAS)
    assert_equals(expected_result, actual_result)


def test_combine_dataframes() -> None:
    """
    Tests data_cleaning.py's combine_dataframes().
    """
    features_data = []
    features_data.append(data_cleaning.get_isolation_percentage(TEST_PANDAS))
    features_data.append(data_cleaning.get_economic_stress_percentage(TEST_PANDAS))
    expected_data = {'post': [FIRST_POST, FIRST_POST, THIRD_POST, THIRD_POST, SECOND_POST, SECOND_POST],
                     'date': [FIRST_DATE, FIRST_DATE, THIRD_DATE, THIRD_DATE, SECOND_DATE, SECOND_DATE], 
                    'percentage': [0.0, 0.0, 2.0, 0.0, 0.0, 0.694444],
                    'type_of_word': ['isolation_total', 'economic_stress_total', 'isolation_total', 'economic_stress_total', 'isolation_total', 'economic_stress_total']}
    expected_result = pd.DataFrame(data=expected_data)
    expected_result = expected_result.reset_index(drop=True)
    actual_result = data_cleaning.combine_dataframes(features_data)
    actual_result = actual_result.reset_index(drop=True)
    assert_equals(expected_result, actual_result)



def main():
    test_get_unique_word_percentage()
    print("Passed get_unique_word_percentage!")
    test_get_isolation_percentage()
    print("Passed get_isolation_percentage!")
    test_get_economic_stress_percentage()
    print("Passed get_economic_stress_percentage!")
    test_get_substance_use_percentage()
    print("Passed get_substance_use_percentage!")
    test_get_domestic_stress_percentage()
    print("Passed get_domestic_stress_percentage!")
    test_get_suicidality_percentage()
    print("Passed get_suicidality_percentage!")
    test_combine_dataframes()
    print("Passed combine_dataframes!")


if __name__ == '__main__':
    main()
