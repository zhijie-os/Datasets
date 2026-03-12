import pandas as pd

# Read the parquet file
df = pd.read_parquet('/mnt/nvme2n1/x30069129/dataset/AIME-24/test.parquet')

# Add extra_info column
extra_info_list = []
for i in range(len(df)):
    extra_info_list.append({
        'index': i,
        'problem_idx': i + 1,
        'problem_type_category': 'math'  # or df.iloc[i]['ability'] if you want to use the ability column
    })

df['extra_info'] = extra_info_list

# Save the updated dataframe
df.to_parquet('/mnt/nvme2n1/x30069129/dataset/AIME-24/test_updated.parquet', index=False)

print("Done! Added extra_info column to the dataframe.")
print(df[['prompt', 'extra_info']].head())
