# Datasets for ACRL and PIPO

Prepared GSM8K and difficult math sets (AIME, AMC, HMMT, MATH-500, Math-500) for ACRL and PIPO following the verl guide line:

https://verl.readthedocs.io/en/latest/preparation/prepare_data.html


The format is 
`
     data = {
            "data_source": data_source,
            "prompt": [{
                "role": "user",
                "content": question
            }],
            "ability": "math",
            "reward_model": {
                "style": "rule",
                "ground_truth": solution
            },
            "extra_info": {
                'split': split,
                'index': idx
            }
`

