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

def unique_topic_percentage_chart_vega(data: pd.DataFrame) -> None:
    """
    Takes the data and plots a chart with ______[TODO]
    """
    print("TYPES")
    print(data.dtypes)
    print("PREDATA: ")
    print(data)
    # data = data.groupby('date', as_index=False).agg({'percentage': 'mean', 'type_of_word': 'first'})
    
    grouped = data.groupby(['date', 'type_of_word'])['percentage'].mean().reset_index()

    # Pivot the DataFrame to have separate columns for each type_of_word
    pivoted = grouped.pivot(index='date', columns='type_of_word', values='percentage').reset_index()

    # Rename the columns to include the prefix 'average_' and fill any missing values with 0
    pivoted.columns = ['date'] + ['average_' + col for col in pivoted.columns[1:]]
    pivoted = pivoted.fillna(0)
   
   #  data.drop('percentage').transform()
    # data.append(grouped)
    print("AFTER: ")
    print(pivoted)

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
    chart = alt.Chart(pivoted).mark_bar().encode(
        x='date:O',
        y='sum(yield):Q',
        color='year:N',
        column='site:N'
    )
    

    chart.save('chart.html')

