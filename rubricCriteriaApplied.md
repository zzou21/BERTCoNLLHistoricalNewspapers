## Rubric:


TODO: Conducted both qualitative and quantitative evaluation with thoughtful discussion (5 pts)

### 1. ML (70 points, requesting 80 points):
- Modular code design with reusable functions and classes rather than monolithic scripts (3 pts)
    - I use reusable functions throughout the project. For one example, see `FineTuneBERT.ipynb` code cell 5, where I wrote an API for BERT fine-tuning since I will be training BERT 5 times using different hyperparameters. I wrote the API so that at each of the 5 instances, I only need to specify the hyperparameters without having to rewrite the training script again. For another example, I replicated the graph training curve function in code cell 11, also in `FineTuneBERT.ipynb`, where I borrowed the function so that I only need to call the graph function, rather than writing graphing function everytime, after I train the model.

- Created baseline model for comparison (e.g., constant prediction, random, simple heuristic) (3 pts)
    - See `baselineBERT.ipynb` file to see the baseline model data that I created, where I use the random named entity frequency shown in a published research paper to ensure that my model is more accurate than at least a random selection of named entities.

- Implemented proper train/validation/test split with documented split ratios (3 pts)
    - Training: 67.69% of data; validation: 15.67%; testing: 16.65%. See `FineTuneBERT.ipynb` code cell 3 for code.

- Tracked and visualized training curves showing loss and/or metrics over time (3 pts)
    - See `FineTuneBERT.ipynb` code cells 12, 15, 18, 21, and 24 for visualizations of training loss and validation score.

- Conducted systematic hyperparameter tuning using validation data or cross-validation (evidence: comparison of multiple configurations) (5 pts)
    - See `FineTuneBERT.ipynb`'s process of testing out 5 different groups of hyperparameters to see which one has the best result. Result presented at the end of this notebook. You can also see my file `hyperparameterComparison.md` for a more detailed record of my hyperparameter tuning process.

- Properly normalized or standardized input features/data appropriate to your modality (3 pts)
    - See `FineTuneBERT.ipynb` code cell 2, 3, and 4.

- Collected or constructed original dataset through substantial engineering effort (e.g., API integration, web scraping, manual annotation/labeling, custom curation) with documented methodology (10 pts)
    - See `LibraryOfCongressDocumentExtraction.ipyunb` file to see my code that uses API call to obtain data from Library of Congress.

- Trained model using GPU/TPU/CUDA acceleration (5 pts)
    - See `FineTuneBERT.ipynb` code cell 9 (and four other subsequent cells since I'm using cuda for model fine-tuning).

- Fine-tuned pretrained model on your dataset (ResNet, BERT, GPT, Llama, etc.) with appropriate adaptation (5 pts)
    - I fine-tuned a pretrained BERT cased model using the CoNLL 2003 NER dataset (the one I'm using to use for my comparison) with adaptation. See `FineTuneBERT.ipynb`.

- Implemented comprehensive text preprocessing and tokenization pipeline (3 pts)
    - See `FineTuneBERT.ipynb` for the `tokenizeAndAlignLabels` and related function.

- Applied in-context learning with few short examples or chain of thought prompting (5 pts)
    - Shown in the file `LLMAPICleaning.py` file between line 36-46.

- Conducted ablation study demonstrating impact of at least two design choices with quantitative comparison (5 pts)
    - See `FineTuneBERT.ipynb`, where I compared five different design choices quantitativly through visualizing their training loss and validation score on graphs. I have summarized the model comparisons and which design choice is the best in the file `hyperparameterComparison.md`.

- Made API calls to state-of-the-art model (GPT-4, Claude, Gemini) with meaningful integration into your system (5 pts)
    -  See `LLMAPICleaning.py` where I call both Mistral and GPT-5-chat to clean OCR data. This cleaning process is important since misspelling significantly decreases the quality of NER.

- Used or fine-tuned a transformer language model (7 pts)
    - I fine-tuned a BERT transformer language model. See `FineTuneBERT.ipynb`. 

- Measured and reported inference time, throughput, or computational efficiency (3 pts)
    - Inference time reported at the end of the file `runFineTunedBERT.ipynb`.

- Completed project individually without a partner (10 pts)
    - This is a solo project

- Used a significant software framework for applied ML not covered in the class (e.g., instead of PyTorch, used Tensorflow; or used JAX, LangChain, etc. not covered in the class) (5 pts)
    -  Using high-performance computing cluster and SLURM job submission script to further customize the GPU and processing power needs beyond API calls or utilizing local machine devices. To increase the speed of generative AI API call inference time when I was performing data cleaning, I used the Mistral open-source model locally by downloading it to the Duke Compute Cluster and requesting more GPUs in processing the data. I performed this because I realized that the API call to an off-site Mistral is too slow. The API call prompt is the same as the file in `LLMAPICleaning.py`, but I had to put in significant time to schedule meeting with OIT DCC staff members to set up my personal Work directory and schedule GPUs in DCC to run the program. I learned to use SLURM script and Linux commands (see my script at `loadDCCCommand.sh` and `mistralAPICall.py`, the former is my job submission script and the latter was my code to use an open-source generative AI locally) to control a high-frequency compute cluster. I believe this is an important ML contribution since, in the future, I know how to request for more GPUs and processing power to run my model and give me more control over calling an API when I can directly control the GPUs and the compute cluster that I'm operating on.