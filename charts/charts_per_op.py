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
# Initial filtering
try:
    data = data[(data['name'] == 'service_time')]
    data = data[data['value.mean'] != '-']
    data = data[data['user-tags.product'] != '-']
except:
    pass
# Fallback for product name
try:
    data['user-tags.product'] = data['meta.tag_product']
except Exception:
    pass
# Convert numeric columns
for col in ['value.50_0', 'value.90_0', 'value.100_0', 'value.mean']:
    try:
        data[col] = data[col].str.replace(',', '').astype(float)
    except:
        pass
operations = data['operation'].unique()
# Output folder
generated_dir = 'generated'
if not os.path.exists(generated_dir):
    os.makedirs(generated_dir)
# Store all stats here
all_stats = []
for op in operations:
    # Filter for the current operation
    op_data = data[data['operation'] == op]
    # Group by `user-tags.product` and take the mean of numeric columns
    grouped = (
        op_data
        .groupby('user-tags.product')[['value.mean', 'value.50_0', 'value.90_0', 'value.100_0']]
        .mean()
        .reset_index()
    )
    # Calculate extra metrics: compare ES vs OS
    grouped['product_lower'] = grouped['user-tags.product'].str.lower()
    if {'elasticsearch', 'opensearch'}.issubset(set(grouped['product_lower'])):
        es_mean = grouped.loc[grouped['product_lower'] == 'elasticsearch', 'value.90_0'].values[0]
        os_mean = grouped.loc[grouped['product_lower'] == 'opensearch', 'value.90_0'].values[0]
        percent_faster_es = ((os_mean - es_mean) / os_mean) * 100
        times_faster_es = os_mean / es_mean
        grouped['percent_faster_es_90_0'] = percent_faster_es
        grouped['times_faster_es_90_0'] = times_faster_es
    else:
        grouped['percent_faster_es_90_0'] = float('nan')
        grouped['times_faster_es_90_0'] = float('nan')
    grouped = grouped.drop(columns=['product_lower'])
    # Add operation column for reference in aggregated CSV
    grouped['operation'] = op
    # Append to list
    all_stats.append(grouped)
    # Create plots
    fig, (ax1, ax2) = plt.subplots(2)
    builder.performance_diff(
        title=op,
        ylabel='Latency p90',
        xlabel='',
        data=op_data,
        value_column='value.90_0',
        ax=ax1,
        operations=[op],
        box_colors=['#005571AA', '#FF7F00AA']
    )
    builder.boxplot(
        title='',
        ylabel='Latency Distribution',
        xlabel='',
        data=op_data,
        value_column='value.mean',
        ax=ax2,
        operations=[op],
        box_colors=['#005571AA', '#FF7F00AA']
    )
    plt.savefig(f"{generated_dir}/{op}.png")
    plt.close(fig)
# Combine and save one big CSV
if all_stats:
    final_df = pd.concat(all_stats, ignore_index=True)
    final_df.to_csv(os.path.join(generated_dir, "all_operations_stats.csv"), index=False)
    