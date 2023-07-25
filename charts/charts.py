import sys
import pandas as pd
import matplotlib.pyplot as plt
import builder


if len(sys.argv) < 2:
    print("Please provide the path to the CSV file as a command line argument.")
    sys.exit(1)


csv_file = sys.argv[1]
data = pd.read_csv(csv_file)

try:
  data = data[(data['name'] == 'service_time')]
  data = data[data['value.mean'] != '-']
  data = data[data['user-tags.product'] != '-']
except:
  pass

try:
  data['user-tags.product'] = data['meta.tag_product']
except Exception as e:
  pass



try:
  data['value.90_0'] = data['value.90_0'].str.replace(',', '').astype(float)
except:
  pass

try:
  data['value.100_0'] = data['value.100_0'].str.replace(',', '').astype(float)
except:
  pass

try:
  data['value.mean'] = data['value.mean'].str.replace(',', '').astype(float)
except:
  pass

try:
  data['value'] = data['value'].str.replace(',', '').astype(float)
except:
  pass

print(data.head())

fig, ((ax1, ax2, ax3), (ax11, ax21, ax31)) = plt.subplots(2,3)


timestamp_sorting = [
      'asc_sort_timestamp',
      'asc_sort_timestamp_can_match_shortcut',
      'asc_sort_timestamp_no_can_match_shortcut',
      'asc_sort_with_after_timestamp',
      'desc_sort_timestamp',
      'desc_sort_timestamp_can_match_shortcut',
      'desc_sort_timestamp_no_can_match_shortcut',
      'desc_sort_with_after_timestamp'
      ]




#sort timestamp
builder.performance_diff(  
      title='Timestamp Sorting', 
      ylabel='Latency p90',
      xlabel='',
      data=data, 
      value_column='value.90_0',
      ax=ax1, 
      operations=timestamp_sorting,
      box_colors=['#005571AA', '#FF7F00AA']
      )

builder.boxplot(
    title='', 
    ylabel='Latency Distribution',
    xlabel='',
    data=data, 
    value_column='value.mean',
    ax=ax11,
    operations=timestamp_sorting,
    box_colors=['#005571AA', '#FF7F00AA']
    )


keyword_sorting = [
        'sort_keyword_can_match_shortcut', 
        'sort_keyword_no_can_match_shortcut'
      ]
# sort keyword
builder.performance_diff(  
      title='Keyword Sorting', 
      ylabel='',
      xlabel='',
      data=data, 
      value_column='value.90_0',
      ax=ax2, 
      operations=keyword_sorting,
      box_colors=['#005571AA', '#FF7F00AA']
      )

# sort keyword
builder.boxplot(
    title='', 
    ylabel='',
    xlabel='',
    data=data, 
    value_column='value.mean',
    ax=ax21,
    operations=keyword_sorting,
    box_colors=['#005571AA', '#FF7F00AA']
    )


numeric_sorting = [
    'sort_numeric_desc', 
    'sort_numeric_asc', 
    'sort_numeric_desc_with_match', 
    'sort_numeric_asc_with_match'
    ]
# sort numeric
builder.performance_diff(  
      title='Numeric Sorting', 
      ylabel='',
      xlabel='',
      data=data, 
      value_column='value.90_0',
      ax=ax3, 
      operations=numeric_sorting,
      box_colors=['#005571AA', '#FF7F00AA']
      )

# sort numeric
builder.boxplot(
    title='', 
    ylabel='',
    xlabel='',
    data=data, 
    value_column='value.mean',
    ax=ax31,
    operations=numeric_sorting,
    box_colors=['#005571AA', '#FF7F00AA']
    )



fig, ((ax1, ax2), (ax11, ax21)) = plt.subplots(2,2)


builder.performance_diff(  
      title='Date Histogram', 
      ylabel='Latency p90',
      xlabel='',
      data=data, 
      value_column='value.90_0',
      ax=ax1, 
      operations=[
      'date_histogram_minute_agg',
      'date_histogram_hourly_agg'
      ],
      box_colors=['#005571AA', '#FF7F00AA']
      )

builder.boxplot(
    title='', 
    ylabel='Latency Distribution',
    xlabel='',
    data=data, 
    value_column='value.mean',
    ax=ax11,
    operations=[
      'date_histogram_minute_agg',
      'date_histogram_hourly_agg'
      ],
    box_colors=['#005571AA', '#FF7F00AA']
    )



builder.performance_diff(  
      title='Date Histogram Composite', 
      ylabel='',
      xlabel='',
      data=data, 
      value_column='value.90_0',
      ax=ax2, 
      operations=[
        'composite-date_histogram-daily', 'composite-date_histogram-monthly', 'composite-date_histogram-weekly'
      ],
      box_colors=['#005571AA', '#FF7F00AA']
      )

builder.boxplot(
    title='', 
    ylabel='',
    xlabel='',
    data=data, 
    value_column='value.mean',
    ax=ax21,
    operations=[
      'composite-date_histogram-daily', 'composite-date_histogram-monthly', 'composite-date_histogram-weekly'
      ],
    box_colors=['#005571AA', '#FF7F00AA']
    )



fig, ((ax1, ax2), (ax11, ax21)) = plt.subplots(2,2)

range_query = [
      'range','range-numeric','keyword-in-range','range_field_conjunction_big_range_big_term_query','range_field_disjunction_big_range_small_term_query','range-auto-date-histo-with-metrics','range_field_conjunction_small_range_big_term_query','range_field_conjunction_small_range_small_term_query'
      ]

builder.performance_diff(  
      title='Range query', 
      ylabel='Latency p90',
      xlabel='',
      data=data, 
      value_column='value.90_0',
      ax=ax1, 
      operations=range_query,
      box_colors=['#005571AA', '#FF7F00AA']
      )

builder.boxplot(
    title='', 
    ylabel='Latency Distribution',
    xlabel='',
    data=data, 
    value_column='value.mean',
    ax=ax11,
    operations=range_query,
    box_colors=['#005571AA', '#FF7F00AA']
    )



builder.performance_diff(  
      title='Range Aggregation', 
      ylabel='',
      xlabel='',
      data=data, 
      value_column='value.90_0',
      ax=ax2, 
      operations=[
      'range-auto-date-histo'
      ],
      box_colors=['#005571AA', '#FF7F00AA']
      )

builder.boxplot(
    title='', 
    ylabel='',
    xlabel='',
    data=data, 
    value_column='value.mean',
    ax=ax21,
    operations=[
      'range-auto-date-histo'
      ],
    box_colors=['#005571AA', '#FF7F00AA']
    )

fig, ((ax1, ax2, ax3), (ax11, ax21, ax31)) = plt.subplots(2,3)


builder.performance_diff(  
      title='Terms Query', 
      ylabel='Latency p90',
      xlabel='',
      data=data, 
      value_column='value.90_0',
      ax=ax1, 
      operations=[
      'term'
      ],
      box_colors=['#005571AA', '#FF7F00AA']
      )

builder.boxplot(
    title='', 
    ylabel='Latency Distribution',
    xlabel='',
    data=data, 
    value_column='value.mean',
    ax=ax11,
    operations=[
      'term'
      ],
    box_colors=['#005571AA', '#FF7F00AA']
    )




builder.performance_diff(  
      title='Terms Aggregation', 
      ylabel='',
      xlabel='',
      data=data, 
      value_column='value.90_0',
      ax=ax2, 
      operations=[
      'multi_terms-keyword',
      'keyword-terms-low-cardinality',
      'keyword-terms'
      ],
      box_colors=['#005571AA', '#FF7F00AA']
      )

builder.boxplot(
    title='', 
    ylabel='',
    xlabel='',
    data=data, 
    value_column='value.mean',
    ax=ax21,
    operations=[
      'multi_terms-keyword',
      'keyword-terms-low-cardinality',
      'keyword-terms'
      ],
    box_colors=['#005571AA', '#FF7F00AA']
    )



builder.performance_diff(  
      title='Terms Agg. (Composite)', 
      ylabel='',
      xlabel='',
      data=data, 
      value_column='value.90_0',
      ax=ax3, 
      operations=[
      'composite-terms',
      'composite-terms-keyword'
      ],
      box_colors=['#005571AA', '#FF7F00AA']
      )

builder.boxplot(
    title='', 
    ylabel='',
    xlabel='',
    data=data, 
    value_column='value.mean',
    ax=ax31,
    operations=[
      'composite-terms',
      'composite-terms-keyword'
      ],
    box_colors=['#005571AA', '#FF7F00AA']
    )



fig, ((ax1, ax2), (ax11, ax21)) = plt.subplots(2,2)


builder.performance_diff(  
      title='Simple Query', 
      ylabel='Latency p90',
      xlabel='',
      data=data, 
      value_column='value.90_0',
      ax=ax1, 
      operations=[
      'query-string-on-message',
      'query-string-on-message-filtered'
      ],
      box_colors=['#005571AA', '#FF7F00AA']
      )

builder.boxplot(
    title='', 
    ylabel='Latency Distribution',
    xlabel='',
    data=data, 
    value_column='value.mean',
    ax=ax11,
    operations=[
      'query-string-on-message',
      'query-string-on-message-filtered'
      ],
    box_colors=['#005571AA', '#FF7F00AA']
    )



builder.performance_diff(  
      title='Simple Query Sorted Numeric', 
      ylabel='',
      xlabel='',
      data=data, 
      value_column='value.90_0',
      ax=ax2, 
      operations=[
      'query-string-on-message-filtered-sorted-num'
      ],
      box_colors=['#005571AA', '#FF7F00AA']
      )

builder.boxplot(
    title='', 
    ylabel='',
    xlabel='',
    data=data, 
    value_column='value.mean',
    ax=ax21,
    operations=[
      'query-string-on-message-filtered-sorted-num'
      ],
    box_colors=['#005571AA', '#FF7F00AA']
    )







plt.show()

