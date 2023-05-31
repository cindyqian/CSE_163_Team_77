"""
Name: Sarah Khan, Cindy Qian, and Junhee Park
Group: P077
Implement main method that analyze pre and post COVID
Reddit threads by performing data cleaning and plotting
charts.
"""
import pandas as pd
import data_cleaning as dc
import chart_plotting as chart


def analyzing_reddit_thread(file_one: str, file_two: str,
                            thread_name: str) -> None:
    """
    This function takes the string parameters called 'file_one'
    which is a file path to the pre-feature data,
    'file_two' which is a file path to the post-feature data, and 'thread_name'
    which is the name of the Reddit thread.
    Create a list of data frames by the percentage of
    isolation, economic stress, substance use, domestic stress,
    and suicidality in the pre-feature dataset.
    Also create a list of data frames by the percentage of isolation,
    economic stress, substance use,
    domestic stress, and suicidality in the post-feature dataset.
    Combine those two lists of data frames and plot the charts.
    """
    # Encoding from:
    # https://stackoverflow.com/questions/5552555/unicodedecodeerror-invalid-continuation-byte
    pre_features = pd.read_csv(file_one, encoding='latin-1')
    post_features = pd.read_csv(file_two, encoding='latin-1')

    # get data for pre features
    pre_dataframes = []
    pre_dataframes.append(dc.get_isolation_percentage(pre_features))
    pre_dataframes.append(dc.get_economic_stress_percentage(pre_features))
    pre_dataframes.append(dc.get_substance_use_percentage(pre_features))
    pre_dataframes.append(dc.get_domestic_stress_percentage(pre_features))
    pre_dataframes.append(dc.get_suicidality_percentage(pre_features))

    all_pre_data = dc.combine_dataframes(pre_dataframes)

    # get data for post features
    post_dataframes = []
    post_dataframes.append(dc.get_isolation_percentage(post_features))
    post_dataframes.append(dc.get_economic_stress_percentage(post_features))
    post_dataframes.append(dc.get_substance_use_percentage(post_features))
    post_dataframes.append(dc.get_domestic_stress_percentage(post_features))
    post_dataframes.append(dc.get_suicidality_percentage(post_features))

    all_post_data = dc.combine_dataframes(post_dataframes)

    # saves 2 charts in seperate files
    pre_file = "pre_" + thread_name
    post_file = "post_" + thread_name
    chart.unique_topic_percentage_chart(all_pre_data, pre_file)
    chart.unique_topic_percentage_chart(all_post_data, post_file)

    chart.unique_topic_percentage_chart_vega(all_pre_data, pre_file)
    chart.unique_topic_percentage_chart_vega(all_post_data, post_file)


def main():
    print('Starting to process data...')
    # thread = addiction
    print('=== ADDICTION THREAD ===')
    print('Beginning to process data for addiction thread...')
    analyzing_reddit_thread("addiction_pre_features.csv",
                            "addiction_post_features.csv", "addiction")
    print('Done processing data for addiction thread...')

    # thread = fitness
    print('=== FITNESS THREAD ===')
    print('Beginning to process data for fitness thread...')
    analyzing_reddit_thread("fitness_pre_features.csv",
                            "fitness_post_features.csv", "fitness")
    print('Done processing data for fitness thread...')

    # thread = parenting
    print('=== PARENTING THREAD ===')
    print('Beginning to process data for parenting thread...')
    analyzing_reddit_thread("parenting_pre_features.csv",
                            "parenting_post_features.csv", "parenting")
    print('Done processing data for parenting thread...')


if __name__ == '__main__':
    main()
