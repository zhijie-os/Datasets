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
        
        # Extract the answer/ground truth
        ground_truth = example['answer']
        
        # Extract problem type (list of subjects)
        problem_types = example.get('problem_type', ['math'])
        # Use the first problem type as the ability
        ability = problem_types[0].lower().replace(' ', '_') if problem_types else 'math'
        
        # Extract problem index
        problem_idx = example.get('problem_idx', idx)
        
        
        # Construct the data in the required format
        data = {
            "data_source": "HMMT25",  # or your dataset name
            "prompt": [{
                "role": "user",
                "content": question
            }],
            "ability": ability,
            "reward_model": {
                "style": "rule",
                "ground_truth": ground_truth
            },
            "extra_info": {
                'split': split,
                'index': idx,
                'problem_idx': problem_idx,
                'problem_types': problem_types,
                'problem_type_count': len(problem_types)
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

    local_dir = args.d

    train_dataset.to_parquet(os.path.join(local_dir, 'test.parquet'))
    # test_dataset.to_parquet(os.path.join(local_dir, 'test.parquet'))


