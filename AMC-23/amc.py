import pandas as pd

# Load and process in one go
df = pd.read_parquet("/mnt/nvme2n1/x30069129/dataset/AMC-23/test.parquet")

# Transform using vectorized operations
processed = df.apply(lambda row: {
    "data_source": "AoPS-AMC",
    "prompt": [{"role": "user", "content": str(row['question'])}],
    "ability": "math",
    "reward_model": {"style": "rule", "ground_truth": str(row['answer'])},
    "extra_info": {
        'split': 'test',
        'index': int(row['id']),
        **({'url': str(row['url'])} if 'url' in row else {})
    }
}, axis=1)

# Convert to DataFrame and save
pd.DataFrame(list(processed)).to_parquet(
    "/mnt/nvme2n1/x30069129/dataset/AMC-23/test_processed.parquet", 
    index=False
)

print(f"Processed {len(df)} records")
