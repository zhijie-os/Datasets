import re
import os
import datasets

from verl.utils.hdfs_io import copy, makedirs
import argparse

# To extract the solution for each prompts in the dataset
# def extract_solution(solution_str):
# ...

def make_map_fn(split):

    def process_fn(example, idx):
        prompt_content = example["prompt"][0]["content"]
        ground_truth = example['reward_model']['ground_truth']
        ability = example['ability'].lower()
        internal_index = example.get('__index_level_0__', str(idx))

        data = {
            "data_source": example['data_source'],
            "prompt": [{
                "role": "user",
                "content": prompt_content
            }],
            "ability": ability,
            "reward_model": {
                "style": "rule",
                "ground_truth": ground_truth
            },
            "extra_info": {
                'split': split,
                'index': idx,
                'internal_index': internal_index
            }
        }
        return data

    return process_fn

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', default=None) # dir
    parser.add_argument("-f", default=None) # format
    parser.add_argument("-p", default=None) # file path


    args = parser.parse_args()



    dataset = datasets.load_dataset(args.f, data_files=args.p)
    train_dataset = dataset['train']
    # test_dataset = dataset['test']

        # Construct a `def make_map_fn(split)` for the corresponding datasets.
    # ...

    train_dataset = train_dataset.map(function=make_map_fn('train'), with_indices=True)
    # test_dataset = test_dataset.map(function=make_map_fn('test'), with_indices=True)

    local_dir = args.local_dir
    hdfs_dir = args.hdfs_dir

    train_dataset.to_parquet(os.path.join(local_dir, 'train.parquet'))
    # test_dataset.to_parquet(os.path.join(local_dir, 'test.parquet'))

    makedirs(hdfs_dir)

    copy(src=local_dir, dst=hdfs_dir)
