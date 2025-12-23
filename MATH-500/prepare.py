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
        # Extract the problem/question
        question = example['problem']
        
        # Extract the solution/ground truth
        ground_truth = example['answer']  # Use 'answer' field for ground truth
        
        # Extract additional information
        subject = example.get('subject', 'math')
        level = example.get('level', 1)
        unique_id = example.get('unique_id', str(idx))
        
        
        # Construct the data in the required format
        data = {
            "data_source": "aime",  # or your dataset name
            "prompt": [{
                "role": "user",
                "content": question
            }],
            "ability": subject.lower(),
            "reward_model": {
                "style": "rule",
                "ground_truth": ground_truth.replace(" ","").strip()
            },
            "extra_info": {
                'split': split,
                'index': idx,
                'unique_id': unique_id,
                'level': level,
                'full_solution': example.get('solution', '')  # Optional: store full solution
            }
        }
        return data
    
    return process_fn

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--local_dir', default=None) # dir
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

    train_dataset.to_parquet(os.path.join(local_dir, 'test.parquet'))
    # test_dataset.to_parquet(os.path.join(local_dir, 'test.parquet'))


