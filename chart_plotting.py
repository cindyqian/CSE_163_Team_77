"""
Name: Sarah Khan, Cindy Qian, and Junhee Park
Group: P077
Implement the functions that visualizes data by plotting charts.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt


def unique_topic_percentage_chart(data: pd.DataFrame, file_name: str) -> None:
    """
    Takes the data and plots a chart with lines for each of
    the total percentages found for the different topic areas.
    Let the x-axis be time and the y-axis be the percentage.
    """
    # Note: Next steps is to make intervals into months for time
    sns.relplot(x="date", y="percentage", kind="line", hue="type_of_word",
                data=data, legend=True, ci=None)
    plt.title("Percentages of Topic Word Usage over Time")
    plt.xlabel("Date")
    plt.ylabel("Percentage")
    plt.savefig(file_name, bbox_inches="tight")


def unique_topic_percentage_chart_vega(data: pd.DataFrame,
                                       file_name: str) -> None:
    """
    Takes the Pandas DataFrame calls 'data' and string value of file name
    calls 'file_name' to plot a chart with lines for each of the
    total percentages found for the different topic areas using Vega Altair.
    Group the datasets by each month.
    The X-Axis is month and the Y-Axis is average percentage.
    """
    pivoted = data.pivot_table(index=['date', 'post'], columns='type_of_word',
                               values='percentage', aggfunc='mean')

    # Reset the index to flatten the pivoted DataFrame
    pivoted = pivoted.reset_index()

    # Rename the columns to include the 'average_' prefix
    pivoted.columns = ['date', 'post'] + ['average_' + col
                                          for col in pivoted.columns[2:]]

    pivoted['date'] = pd.to_datetime(pivoted['date'], format="mixed")

    # Extract the month from the 'date' column and create a new 'month' column
    pivoted['month'] = pivoted['date'].dt.to_period('M')

    grouped = pivoted.groupby('month', as_index=False)[pivoted.
                                                       columns[2:]].mean()

    # Dropping any malformatted data
    grouped = grouped[grouped['month'] != 0]

    # Reshape the DataFrame using melt
    melted = grouped.melt(id_vars=['month'], var_name='type_of_word',
                          value_name='average_stat')

    # Sort the DataFrame by 'month' and 'type_of_word' columns
    melted = melted.sort_values(by=['month',
                                    'type_of_word']).reset_index(drop=True)
    melted['month'] = melted['month'].astype(str)

    melted = melted[melted['type_of_word'] != 'average_n_unique_words']
    chart = alt.Chart(melted).mark_line().encode(
        x='month',
        y='average_stat',
        column='type_of_word',
    ).properties(
        width=200
    )

    file = 'chart_' + file_name + '.html'
    chart.save(file)
