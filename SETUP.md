### Set Up

To set up the project, you need:

1. The following libraries:
- torch
- transformers
- json
- time
- tqdm

You also need Python.

Some of them should come as default when installing Python.

2. Then, we need to create the data files. I have written a Python script to turn my TXTs into one merged JSON. You can run the code in `data/txToJSON.py` to create that one merged JSON. I have also already run the code and generated a merged JSON, if you don't want to generate one yourself. You can find the already merged JSON at `data/newspaperCleanedContent.json`.

3. Then, you need to find the fine-tuned BERT that was the most effective model after I tested five different fine-tuning hyperparameter configurations. You can find the fine-tuned BERT model in the `models` directory. Since I am using GitHub, I do not have the storage to store the entire fine-tuned model on GitHub, so the `models` directory contains a Markdown file with links to the models that you can download. You then need to find the model labeled: `best performing model` and download it.

4. After downloading the best performing model, you need to use the Jupyter Notebook `runFineTunedBERT.ipynb` found in the `notebooks` directory, where you will need to put in the file path for the merged JSON text data file, the file path to the model that you've downloaded, and the file path that you want to store the labeled NER tags.

5. After running `runFineTunedBERT.ipynb`, you can find the labeled NER tags in the JSON file that you specified.