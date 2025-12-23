import pandas as pd
import json

# Read the parquet file
df = pd.read_parquet('/mnt/nvme2n1/x30069129/dataset/AIME-25/test.parquet')

# Transform the data
transformed_data = []
for idx, row in df.iterrows():
    # Parse verification_info - assuming it's a JSON string
    try:
        verification_info = json.loads(row['verification_info'])
    except:
        verification_info = {}
    
    transformed = {
        "data_source": "aime",
        "prompt": [{
            "role": "user",
            "content": row['prompt'].replace("Problem: ", "")
        }],
        "ability": "math",
        "reward_model": {
            "style": "rule",
            "ground_truth": verification_info.get('ground_truth', '')
        },
        "extra_info": {
            'split': 'train',
            'index': idx,
            'original_problem_id': row['problem_id'],
            'original_task_type': row['task_type']
        }
    }
    transformed_data.append(transformed)

transformed_df = pd.DataFrame(transformed_data)
transformed_df.to_parquet("test_fixed.parquet", index=False)
