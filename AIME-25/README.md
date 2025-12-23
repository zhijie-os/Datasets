---
dataset_info:
  features:
  - name: problem_id
    dtype: string
  - name: prompt
    dtype: string
  - name: task_type
    dtype: string
  - name: verification_info
    dtype: string
  splits:
  - name: train
    num_bytes: 13997
    num_examples: 30
  download_size: 10729
  dataset_size: 13997
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
