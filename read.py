import pandas as pd
import os

import argparse



pd.set_option('display.max_columns', None)

parser = argparse.ArgumentParser()
parser.add_argument('--file', default=None) # dir
args = parser.parse_args()


# Read the entire file into a DataFrame
df = pd.read_parquet("/mnt/nvme2n1/x30069129/dataset"+args.file)
print(df)

