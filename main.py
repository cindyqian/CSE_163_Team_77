# import pandas as pd
# import data_cleaning as data_cleaning
# import chart_plotting as chart


# def main():
#     print("here")

#     # we have 2 files,
#     #   1 file of all pre-covid subreddit data (manually combined)
#     #   1 file of all post-covid subreddit data (manually combined)
#     # for each file, we run all data_cleaning methods on the data,
#     # this gives us the percentage of topic words in that file.
#     # This gives us 5, 2-column dataframes with the percentages of
#     # each topic as the second column of each dataframe.abs

#     # we then combine all 5 dataframes into one for each file.
#     # This gives us 2 dataframes with 6 columns each.abs

    
#     # We plot each cof the 6 columns as a trendline on a chart.abs
#     # This gives us 2 charts, each with 5 trendlines.

#     # We can then compare the difference in trendlines between
#     # pre and post covid.

#     pre_features = pd.read_csv("test_addiction_pre_features.csv")
#     post_features = pd.read_csv("test_addiction_post_features.csv")
#     print(pre_features.head())

#     # result = data_cleaning.get_unique_word_percentage(pre_features)
    
#     # get data for pre features
#     all_percentage_dataframes_pre = []
#     all_percentage_dataframes_pre.append(data_cleaning.get_unique_word_percentage(pre_features))
#     all_percentage_dataframes_pre.append(data_cleaning.get_isolation_percentage(pre_features))
#     all_percentage_dataframes_pre.append(data_cleaning.get_economic_stress_percentage(pre_features))
#     all_percentage_dataframes_pre.append(data_cleaning.get_substance_use_percentage(pre_features))
#     all_percentage_dataframes_pre.append(data_cleaning.get_domestic_stress_percentage(pre_features))
#     all_percentage_dataframes_pre.append(data_cleaning.get_suicidality_percentage(pre_features))

#     all_pre_data = data_cleaning.combine_dataframes(all_percentage_dataframes_pre)
#     print("Predata:")
#     print(all_pre_data.head())

#     # get data for post features
#     all_percentage_dataframes_post = []
#     all_percentage_dataframes_post.append(data_cleaning.get_isolation_percentage(post_features))
#     all_percentage_dataframes_post.append(data_cleaning.get_economic_stress_percentage(post_features))
#     all_percentage_dataframes_post.append(data_cleaning.get_substance_use_percentage(post_features))
#     all_percentage_dataframes_post.append(data_cleaning.get_domestic_stress_percentage(post_features))
#     all_percentage_dataframes_post.append(data_cleaning.get_suicidality_percentage(post_features))

#     all_post_data = data_cleaning.combine_dataframes(all_percentage_dataframes_post)

#     # saves 2 charts in seperate files
#     # UNCOMMENT LINES 56-57
#     # chart.unique_topic_percentage_chart(all_pre_data, "pre")
#     # chart.unique_topic_percentage_chart(all_post_data, "post")

#     # chart.unique_topic_percentage_chart_vega(pre_features)
#     # chart.unique_topic_percentage_chart_vega(data_cleaning.get_isolation_percentage(pre_features))
#     chart.unique_topic_percentage_chart_vega(all_pre_data)


# if __name__ == '__main__':
#     main()
    

"""
Name: Sarah Khan, Cindy Qian, and Junhee Park
Group: P077
...
"""
import pandas as pd
import data_cleaning as data_cleaning
import chart_plotting as chart


def analyzing_reddit_thread(file_one: str, file_two: str) -> None:
    pre_features = pd.read_csv(file_one)
    post_features = pd.read_csv(file_two)
    print(pre_features.head())
    
    # get data for pre features
    all_percentage_dataframes_pre = []
    all_percentage_dataframes_pre.append(data_cleaning.get_unique_word_percentage(pre_features))
    all_percentage_dataframes_pre.append(data_cleaning.get_isolation_percentage(pre_features))
    all_percentage_dataframes_pre.append(data_cleaning.get_economic_stress_percentage(pre_features))
    all_percentage_dataframes_pre.append(data_cleaning.get_substance_use_percentage(pre_features))
    all_percentage_dataframes_pre.append(data_cleaning.get_domestic_stress_percentage(pre_features))
    all_percentage_dataframes_pre.append(data_cleaning.get_suicidality_percentage(pre_features))

    all_pre_data = data_cleaning.combine_dataframes(all_percentage_dataframes_pre)

    # get data for post features
    all_percentage_dataframes_post = []
    all_percentage_dataframes_post.append(data_cleaning.get_isolation_percentage(post_features))
    all_percentage_dataframes_post.append(data_cleaning.get_economic_stress_percentage(post_features))
    all_percentage_dataframes_post.append(data_cleaning.get_substance_use_percentage(post_features))
    all_percentage_dataframes_post.append(data_cleaning.get_domestic_stress_percentage(post_features))
    all_percentage_dataframes_post.append(data_cleaning.get_suicidality_percentage(post_features))

    all_post_data = data_cleaning.combine_dataframes(all_percentage_dataframes_post)

    # saves 2 charts in seperate files
    chart.unique_topic_percentage_chart(all_pre_data, "pre")
    chart.unique_topic_percentage_chart(all_post_data, "post")

    chart.unique_topic_percentage_chart_vega(all_pre_data)


def main():
    print("here")

    # we have 2 files,
    #   1 file of all pre-covid subreddit data (manually combined)
    #   1 file of all post-covid subreddit data (manually combined)
    # for each file, we run all data_cleaning methods on the data,
    # this gives us the percentage of topic words in that file.
    # This gives us 5, 2-column dataframes with the percentages of
    # each topic as the second column of each dataframe.abs

    # we then combine all 5 dataframes into one for each file.
    # This gives us 2 dataframes with 6 columns each.abs

    
    # We plot each cof the 6 columns as a trendline on a chart.abs
    # This gives us 2 charts, each with 5 trendlines.

    # We can then compare the difference in trendlines between
    # pre and post covid.


    # thread = addiction
    analyzing_reddit_thread("addiction_pre_features.csv", "addiction_post_features.csv")

    # fitness
    analyzing_reddit_thread("fitness_pre_featuress.csv", "fitness_post_featuress.csv")

    # parenting
    analyzing_reddit_thread("parenting_pre_featuress.csv", "parentingn_post_features.csv")



if __name__ == '__main__':
    main()