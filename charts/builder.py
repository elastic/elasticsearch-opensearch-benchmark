from scipy.stats import ttest_ind

def performance_diff(title, ylabel, xlabel, ax, operations, box_colors, data, value_column='value.90_0'):
  """
  Calculate and visualize performance difference between two products (Elasticsearch and OpenSearch).

  Parameters:
      title (str): Title for the plot.
      ylabel (str): Label for the y-axis of the plot.
      xlabel (str): Label for the x-axis of the plot.
      ax (matplotlib.axes._subplots.AxesSubplot): Matplotlib AxesSubplot object to plot the bar chart.
      operations (list): List of operations to include in the analysis.
      box_colors (list): List of colors for the bars in the bar chart.
      data (pandas.DataFrame): DataFrame containing performance data.
      value_column (str, optional): The column in the DataFrame containing the performance values.
                                    Default is 'value.90_0'.

  Returns:
      None: This function does not return anything. It prints the results and plots the bar chart.

  Note:
      The function performs a t-test to compare the 90th percentile latency of Elasticsearch (es) and
      OpenSearch (va) for the specified operations. It then calculates the percentage difference in
      performance between the two products and plots the mean performance values of each product as
      a bar chart.
  """  

  data = data[data['operation'].isin(operations)]

  es = data[data['user-tags.product']=='Elasticsearch']
  va = data[data['user-tags.product']=='OpenSearch']

  ttest = ttest_ind(es[value_column], va[value_column])

  es_mean = es[value_column].mean()
  va_mean = va[value_column].mean()

  performance_difference_pct = 100 * (abs(va_mean - es_mean)/ ((es_mean+va_mean)/2)) 

  print(f"===== {title} - {performance_difference_pct:.1f}% ")
  print(f"===== (90th percentile latency of {es_mean:.0f}ms vs. {va_mean:.0f}ms, p<0.01) p={ttest.pvalue:.5f} | Samples: {len(data.index)*100} requests")

  grouped_data = data.groupby('user-tags.product')[value_column].mean().reset_index()

  ax.bar(grouped_data['user-tags.product'], grouped_data[value_column], color=box_colors)

  ax.set_title(title)
  ax.set_ylabel(ylabel)
  ax.tick_params(axis='both', labelsize=8)



def boxplot(title, ylabel, xlabel, data, value_column, ax, operations, box_colors):
  """
  Create a box plot (box-and-whisker plot with mean line) to visualize the distribution of performance values
  for different products (Elasticsearch and OpenSearch) and compare their distributions.

  Parameters:
      title (str): Title for the plot.
      ylabel (str): Label for the y-axis of the plot.
      xlabel (str): Label for the x-axis of the plot.
      data (pandas.DataFrame): DataFrame containing performance data.
      value_column (str): The column in the DataFrame containing the performance values.
      ax (matplotlib.axes._subplots.AxesSubplot): Matplotlib AxesSubplot object to plot the box plot.
      operations (list): List of operations to include in the analysis.
      box_colors (list): List of colors for the boxes in the box plot.
  """

  data = data[(data['operation'].isin(operations))]

  grouped_data = data.groupby('user-tags.product')[value_column].apply(list).reset_index(name=value_column)
  
  bp = ax.boxplot(
      grouped_data[value_column], 
      labels=grouped_data['user-tags.product'], 
      patch_artist=True,
      showmeans=True,
      meanline=True,
      notch=False,
      medianprops = {'linestyle': '-', 'linewidth': 1, 'color': 'black'},
      flierprops={'marker': '.', 'markersize': 1},
      meanprops={'linestyle': ':', 'linewidth': 1, 'color': 'white'}
      )

  for box, color in zip(bp['boxes'], box_colors):
      box.set(facecolor=color)

  for median in bp['medians']:
    median.set_color('black')

  ax.set_title(title)
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  ax.tick_params(axis='both', labelsize=8)



