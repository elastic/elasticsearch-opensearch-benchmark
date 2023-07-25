from scipy.stats import ttest_ind


def performance_diff(title, ylabel, xlabel, ax, operations, box_colors, data, value_column='value.90_0'):
  
  data = data[data['operation'].isin(operations)]

  es = data[data['user-tags.product']=='Elasticsearch']
  va = data[data['user-tags.product']=='OpenSearch']

  ttest = ttest_ind(es[value_column], va[value_column])

  es_mean = es[value_column].mean()
  va_mean = va[value_column].mean()

  performance_difference_pct = 100 * (abs(va_mean - es_mean)/ ((es_mean+va_mean)/2)) 


  print(f"===== {title} - {performance_difference_pct:.1f}% ")
  print(f"===== (90th percentile latency of {es_mean:.0f}ms vs. {va_mean:.0f}ms, p<0.01) p={ttest.pvalue:.5f} | Samples: {len(data.index)*100} requests")
  #column = 'value.90_0'
  #data.loc[:, column] = 1/data.loc[:, value_column] 
  #data.loc[:, column] = ( data[column] - data[column].min() ) / (data[column].max() - data[column].min())

  grouped_data = data.groupby('user-tags.product')[value_column].mean().reset_index()

  ax.bar(grouped_data['user-tags.product'], grouped_data[value_column], color=box_colors)

  ax.set_title(title)
  ax.set_ylabel(ylabel)
  #ax.set_ylim([0,1])
  ax.tick_params(axis='both', labelsize=8)



def boxplot(title, ylabel, xlabel, data, value_column, ax, operations, box_colors):

  data = data[(data['operation'].isin(operations))]

  grouped_data = data.groupby('user-tags.product')[value_column].apply(list).reset_index(name=value_column)
  
  bp = ax.violinplot(
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



