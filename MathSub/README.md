---
license: apache-2.0
language:
- en
---
# Dataset Summary

This dataset is a subset of the Klear-Reasoner Math RL dataset.  
The full dataset contains approximately 88K entries, while this release includes a 30K-entry subset.  

The subset was obtained by filtering the outputs of DeepSeek-R1-0120. For each prompt, DeepSeek-R1-0120 generated 16 responses, and we retained only those responses where the majority of completions passed a rule-based validator designed for mathematical correctness and format compliance.  

You can load the dataset using:

```python
from datasets import load_dataset
dataset = load_dataset("Kwai-Klear/KlearReasoner-MathSub-30K")
```
See our paper and GitHub repository for more details.  

| Resource | Link |
|---|---|
| 📝 Preprints | [Paper](https://arxiv.org/pdf/2508.07629) |
| 🤗 Daily Paper | [Paper](https://huggingface.co/papers/2508.07629) |
| 🤗 Model Hub | [Klear-Reasoner-8B](https://huggingface.co/Kwai-Klear/Klear-Reasoner-8B) |
| 🤗 Dataset Hub | [Math RL](https://huggingface.co/datasets/Kwai-Klear/KlearReasoner-MathSub-30K) |
| 🤗 Dataset Hub | [Code RL](https://huggingface.co/datasets/Kwai-Klear/KlearReasoner-CodeSub-15K) |
| 🐛 Issues & Discussions | [GitHub Issues](https://github.com/suu990901/KlearReasoner/issues) |
| 📧 Contact | suzhenpeng13@163.com |

## Data Fields

- **data_source** (string) — The source identifier for the sample.  
- **prompt** (list of dict) — The input prompt, stored as a list of message objects in chat format.  
- **ability** (string) — The skill or task category associated with the sample.  
- **reward_model** (dict) — Information about the ground truth or reward signal.  
  - **ground_truth** (string) — The expected correct answer (may include LaTeX formatting).  
  - **style** (string) — The method or type of evaluation, e.g., "rule".  
- **index_level_0** (int) — An internal index or unique identifier for the sample.  

## Demonstration of Data Quality

This dataset contains exclusively high-quality, filtered samples.  
All samples have been selected to ensure accurate reward signals for reinforcement learning, following the gradient-preserving clipping policy optimization (GPPO) method introduced in our paper. Models trained using this dataset achieve strong generalization and reliable performance on a range of math reasoning tasks.  

## Citation
If you find this work helpful, please cite our paper:
```bibtex
@misc{su2025cegppocontrollingentropygradientpreserving,
      title={CE-GPPO: Controlling Entropy via Gradient-Preserving Clipping Policy Optimization in Reinforcement Learning}, 
      author={Zhenpeng Su and Leiyu Pan and Minxuan Lv and Yuntao Li and Wenping Hu and Fuzheng Zhang and Kun Gai and Guorui Zhou},
      year={2025},
      eprint={2509.20712},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2509.20712}, 
}
```


```bibtex
@article{DBLP:journals/corr/abs-2508-07629,
  author       = {Zhenpeng Su and
                  Leiyu Pan and
                  Xue Bai and
                  Dening Liu and
                  Guanting Dong and
                  Jiaming Huang and
                  Wenping Hu and
                  Fuzheng Zhang and
                  Kun Gai and
                  Guorui Zhou},
  title        = {Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving
                  Clipping Policy Optimization},
  journal      = {CoRR},
  volume       = {abs/2508.07629},
  year         = {2025},
  url          = {https://doi.org/10.48550/arXiv.2508.07629},
  doi          = {10.48550/ARXIV.2508.07629},
  eprinttype    = {arXiv},
  eprint       = {2508.07629},
  timestamp    = {Sat, 13 Sep 2025 14:46:27 +0200},
  biburl       = {https://dblp.org/rec/journals/corr/abs-2508-07629.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```

