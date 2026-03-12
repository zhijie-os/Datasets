import pandas as pd

def rewrite_data_source(input_file, output_file, new_value="aime24"):
    df = pd.read_parquet(input_file)
    
    # Replace all values in data_source column
    df['data_source'] = new_value
    
    df.to_parquet(output_file, index=False)
    print(f"Rewrote data_source column to '{new_value}'")
    return df

# Usage
rewrite_data_source(
    input_file="/mnt/nvme2n1/x30069129/dataset/MATH-500/test.parquet",
    output_file="/mnt/nvme2n1/x30069129/dataset/MATH-500/test_updated.parquet",
    new_value="MATH_500"
)
