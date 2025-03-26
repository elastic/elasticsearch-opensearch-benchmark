import os
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

operations = data['operation'].unique()

generated_dir = 'generated'
if not os.path.exists(generated_dir):
   os.makedirs(generated_dir)

for op in operations:
    fig, (ax1, ax2) = plt.subplots(2)
    builder.performance_diff(
        title=op,
        ylabel='Latency p90',
        xlabel='',
        data=data,
        value_column='value.90_0',
        ax=ax1,
        operations=[op],
        box_colors=['#005571AA', '#FF7F00AA']
    )

    builder.boxplot(
        title='',
        ylabel='Latency Distribution',
        xlabel='',
        data=data,
        value_column='value.mean',
        ax=ax2,
        operations=[op],
        box_colors=['#005571AA', '#FF7F00AA']
    )
    plt.savefig(f"{generated_dir}/{op}.png")
