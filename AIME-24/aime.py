import pandas as pd
import json

# Load the AIME-24 data
df = pd.read_parquet("/mnt/nvme2n1/x30069129/dataset/AIME-24/test.parquet")

# Parse JSON strings to dictionaries
def parse_json(item):
    if isinstance(item, str):
        return json.loads(item)
    return item

df['reward_model'] = df['reward_model'].apply(parse_json)

# Save back
df.to_parquet("/mnt/nvme2n1/x30069129/dataset/AIME-24/test_fixed.parquet")
