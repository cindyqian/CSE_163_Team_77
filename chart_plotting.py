# import data_cleaning from data_cleaning
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from vega_datasets import data

def unique_topic_percentage_chart(data: pd.DataFrame, file_name: str) -> None:
    """
    Takes the data and plots a chart with lines for each of
    the total percentages found for the different topic areas.
    Let the x-axis be time and the y-axis be the percentage.
    """

    # Note: Make intervals into months for time
    sns.relplot(x="date", y="percentage", kind="line", hue="type_of_word", data=data, legend=True)
    plt.title("Percentages of Topic Word Usage over Time")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.savefig(file_name, bbox_inches="tight")

def unique_topic_percentage_chart_vega(data: pd.DataFrame, file_name: str) -> None:
    """
    Takes the data and plots a chart with ______[TODO]
    """
    # print("TYPES")
    # print(data.dtypes)
    print("PREDATA: ")
    print(data)

    # example = data[data['date'] =='2019/09/11']
    # print("EXAMPLE")
    # print(example)
    # example = example.groupby('post')
    # print(example)
    # data = data.groupby('date', as_index=False).agg({'percentage': 'mean', 'type_of_word': 'first'})
    
    # grouped = data.groupby(['date', 'type_of_word'])['percentage'].mean().reset_index()

    # # Pivot the DataFrame to have separate columns for each type_of_word
    # pivoted = grouped.pivot(index='date', columns='type_of_word', values='percentage').reset_index()
    # print("SOFAR: ")
    # print(pivoted)

    # # Add a new column for the average percentage of all type_of_words
    # numeric_columns = pivoted.columns[1:]  # Exclude the 'date' column
    # pivoted['average_percentage'] = pivoted[numeric_columns].mean(axis=1)
    pivoted = data.pivot_table(index=['date', 'post'], columns='type_of_word', values='percentage', aggfunc='mean')

    # Reset the index to flatten the pivoted DataFrame
    pivoted = pivoted.reset_index()

    # Rename the columns to include the 'average_' prefix
    pivoted.columns = ['date', 'post'] + ['average_' + col for col in pivoted.columns[2:]]

    # Print the resulting DataFrame
    # print(pivoted)
   
   #  data.drop('percentage').transform()
    # data.append(grouped)
    print("AFTER: ")
    print(pivoted)
    pivoted['date'] = pd.to_datetime(pivoted['date'])

    # Extract the month from the 'date' column and create a new 'month' column
    pivoted['month'] = pivoted['date'].dt.to_period('M')

    grouped = pivoted.groupby('month', as_index=False)[pivoted.columns[2:]].mean()
    # Dropping any malformatted data
    grouped = grouped[grouped['month'] != 0]

    print("GROUP: ")
    print(grouped)

    # Reshape the DataFrame using melt
    melted = grouped.melt(id_vars=['month'], var_name='type_of_word', value_name='average_stat')

    # Sort the DataFrame by 'month' and 'type_of_word' columns
    melted = melted.sort_values(by=['month', 'type_of_word']).reset_index(drop=True)

    print("MELTED")
    print(melted)

    # chart = alt.Chart(data).mark_rect().encode(
    #     alt.X('date:O').title('date'),
    #     alt.Y('author:O').title('author'),
    #     alt.Color('isolation_total:Q').title('posts related to isolation')
    # )
    # THIS WORKED WITH JUST DATA
    # chart = alt.Chart(data).mark_rect().encode(
    #     x='date',
    #     y='type_of_word',
    #     color='percentage'
    # )
    # chart = alt.Chart(data).mark_rect().encode(
    #     x='date:O',
    #     y='author:O',
    #     color='isolation_total:Q'
    # )
    # chart = alt.Chart(data).mark_rect().encode(
    #     alt.X("yearmonth(date):T").title("Month"),
    #     y='type_of_word',
    #     color='percentage'
    # )
    # melted = melted[melted['month'].dt.year.isin([2018, 2019])]
    melted['month'] = melted['month'].astype(str)
    # chart = alt.Chart(melted).mark_bar().encode(
    #     # x='month:O',
    #     # y='average_stat:Q',
    #     # color='year(month):N',
    #     # column='type_of_word:N'
    #     alt.X('month:N', title='Month'),
    #     alt.Y('average_stat:Q', title='Average Stat', scale=alt.Scale(domain=[0, 100])),
    #     alt.Color('month:N', scale=alt.Scale(domain=['2018', '2019'], range=['#1f77b4', '#ff7f0e'])),
    #     alt.Column('type_of_word:N')
    # ).properties(
    #     width=200
    # )

    # chart2 = alt.Chart(melted).mark_bar().encode(
    #     # x='month:O',
    #     # y='average_stat:Q',
    #     # color='year(month):N',
    #     # column='type_of_word:N'
    #     x='month',
    #     y='average_stat',
    #     column='type_of_word',
    # ).properties(
    #     width=200
    # )
    melted = melted[melted['type_of_word'] != 'average_n_unique_words']
    chart2 = alt.Chart(melted).mark_line().encode(
        # x='month:O',
        # y='average_stat:Q',
        # color='year(month):N',
        # column='type_of_word:N'
        x='month',
        y='average_stat',
        column='type_of_word',
    ).properties(
        width=200
    )

    # Want a schema:
    # date | average | type_of_word (so that there are five )
    

    # chart.save('chart.html')
    file = 'chart_' + file_name + '.html'
    chart2.save(file)

