---
dataset_info:
  features:
  - name: problem_idx
    dtype: int64
  - name: problem
    dtype: string
  - name: answer
    dtype: string
  - name: problem_type
    sequence: string
  splits:
  - name: test
    num_bytes: 0
    num_examples: 30
  download_size: 0
  dataset_size: 0
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test/test.jsonl
license: cc-by-nc-sa-4.0
language:
- en
pretty_name: HMMT February 2025
size_categories:
- n<1K
---

### Homepage and repository

- **Homepage:** [https://matharena.ai/](https://matharena.ai/)
- **Repository:** [https://github.com/eth-sri/matharena](https://github.com/eth-sri/matharena)

### Dataset Summary

This dataset contains the questions from HMMT February 2025 used for the MathArena Leaderboard

### Data Splits & Files

- **test split**: `data/test/test.jsonl` (30 samples)

### Fields
- `problem_idx` (int): Index of the problem
- `problem` (str): Full problem statement
- `answer` (str): Ground-truth answer
- `problem_type` (sequence[string]): e.g. "Combinatorics", "Number Theory", "Algebra", "Geometry"

### Licensing Information

This dataset is licensed under the Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Please abide by the license when using the provided data.

### Citation Information

```
@misc{balunovic_srimatharena_2025,
  title = {MathArena: Evaluating LLMs on Uncontaminated Math Competitions},
  author = {Mislav Balunović and Jasper Dekoninck and Ivo Petrov and Nikola Jovanović and Martin Vechev},
  copyright = {MIT},
  url = {https://matharena.ai/},
  publisher = {SRI Lab, ETH Zurich},
  month = feb,
  year = {2025},
}
```
