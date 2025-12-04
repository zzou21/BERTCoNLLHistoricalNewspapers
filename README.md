### CS 372 Final Project:
### Title: Using BERT to Identify Named Entities in Historical Newspapers

#### Description and What-it-Does
This project uses the BERT encoder-only Transformer language model architecture to understand whether there is a congruency between the language used in newspaper writing between 1890 and 1930 versus the general public writing of today. Language usage, in the context of this project, is defined as whether Named Entities have been used similarly.

To achieve this, this project will focus on three types of Named Entites: Person, Location, and Organization.

Ultimately, this project hopes to show that, despite the common perception that language changes frequently, there is actually a higher-than-expected level of continuity across time.

This project trains a BERT cased model on the CoNLL 2003 model and then use the fine-tuned model to label named entities of newspapers between 1890 and 1930 United States. The reason why the model is not trained on data between 1890-1930 is that I would like to see if a model familiar with only the contemporary language could still understand the word choices about a century ago.

The project then compares the performance of the fine-tuned BERT against the performance of Stanford NER, an existing NER tool that has been regarded as a high-accuracy NER tool.

#### File Structure
<b><i>Directories:</i></b>

<b><i>Top-Level Directory files:</i></b>
- `README.md`: contains documentation for the project.
- `rubricCriteriaApplied.md`: contains elements from the ML section of the rubric that I'm applying to be credited for.
- `ATTRIBUTION.md`: contains my attribution to the various sources of my code.
- `SETUP.md`: contains directions on setting up the project

<b><i>Data</i></b> This directory contains NER data files and code used to obtain and clean the newspaper corpus.
- `baselineLabelingStorageJSON.json`: contains the baseline NER labels.
- `fineTunedBERTPrediction.json`: contains NER labels conducted by the best-performing fine-tuned BERT model.
- `LibraryOfCongressDocumentExtraction.ipynb`: contains the code for using API to call Library of Congress's newspaper database.
- `LLMAPICleaning.py`: contains code to call a generative AI's API to clean OCR-ed newspaper texts obtained from `LibraryOfCongressDocumentExtraction.ipynb`.
- `newspaperCleanedContent.json`: contains 529 pages of cleaned text content of historical US newspapers. This is the corpus that the project is using.
- `stanfordTaggingMerged(UseInEvaluation).json`: contains the Named Entities that Stanford NER labeled. This data is used as a reference during evaluation to compare how my model's Named Entities labels perform.
- `LAoilNewspaperTXTOutputCleaned`: contains the folder of newspaper content as cleaned TXT files. They are the same information as the `newspaperCleanedContent.json`.

<b><i>DCCMistral</i></b> This directory contains the code needed to run the Mistral open-source generative model to clean textual OCR data locally.
- `loadDCCComand.sh`: contains the code that customizes GPU, memory, and other compute cluster parameters when submitting a computation job to DCC.
- `mistralAPICall.py`: contains the Python code that was submitted to DCC to process. 

<b><i>docs</i></b> This directory contains documentations in both TXT and Markdown formats.
- `hyperparameterComparison.md`: contains summaries of the metrics of my hyperparameter tests performed on five different training iterations, each using a different set of hyperparameters.
- `requirements.txt`: contains the required systems and libraries needed to run my program.

<b><i>models</i></b> This directory contains links to download models that I've built.
- `linksToModels.md`: contains a Markdown file with link to my model.

<b><i>notebooks</i></b> This directory contains all Jupyter Notebooks used in this project.
- `baselineBERT.ipynb`: contains the code used to generate a baseline metrics for NER labels.
- `entitiesOutput.json`: contains the Named Entities that my trained BERT model labeled.
- `evaluation.ipynb`: contains the code and qualitative discussion used to perform three evaluation methods to evaluate my trained model.
- `FineTuneBERT.ipynb`: contains the code used to fine-tune BERT using the CoNLL 2003 dataset and the code used to perform five different training iterations using different hyperparameters.
- `runFineTunedBERT.ipynb`: contains the code used to run fine-tuned BERT and calculate average inference time.

<b><i>src</i></b> This directory contains all Python files used in this project.
- `txtToJSON.py`: contains Python code to turn newspaper pages stored as TXTs into one JSON for easier access.

<b><i>video</i></b> This directory contains links to my two videos.
- `videoLinks.md`: contains a Markdown file with links to the two videos that I made.


#### Research Question and Utility

This project addresses a significant question in linguistic and media studies research because a common conception in language usage is that language changes over time, and the writing of one time period (say 21st century writing) is different from those a century ago (say the 1890s and 1900s, the time period that this project addresses). There are many metrics to measure whether language has changed, and this project applies Named Entity Recognition (NER) to see if Named Entities have been used in the same way in language over time. This project tests whether this conception is actually true. To test this question, I train a BERT on the CoNLL 2003 database (to represent modern language usage) and then apply this fine-tuned model on US newspapers between 1892 and 1930 that I obtained from the Library of Congress. To focus my analysis, I specify my work on three types of Named Entities: Person, Organization, and Location. If the model has a high level of accuracy in identifying NERs in my newspaper data, then it shows that the use of Named Entities hasn't changed much over time.

#### Quick Start
You can run the model through following the step-by-step guide in `FineTuneBERT.ipynb` to create your own fine-tuned BERT on the CoNLL 2003 dataset and compare which hyperparameter setup is the most suitable for you. I have stored the best model in the file `linksToModels.md` in the directory `models`, and you can download the model there.

You can find the newspaper cleaned OCR texts from the JSON file `newspaperCleanedContent.json` file in the `data` director. This data was created from the files `LibraryOfCongressDocumentExtraction.ipynb`, `LLMAPICleaning.py`, and `txtToJSON.py`, and you do not need to run these files again.

After preparing your model and your data, you can run the file `runFineTunedBERT.ipynb` to test the NER abilities. NER taggs would be stored in a JSON file of your preference set in `runFineTunedBERT.ipynb`.


#### Video links:
You can find videos in the file `videoLinks.md` in the directory `video`. Links to videos:

- 3-5 min demo video link: [https://duke.box.com/s/34uykhrp4wik4yb18gf81tka5mcs4ehe](https://duke.box.com/s/34uykhrp4wik4yb18gf81tka5mcs4ehe)
- 5-10 min technical walkthrough video link: [https://duke.box.com/s/ldl0tjd2q41soa3ckqrmfp3wb38q2z19](https://duke.box.com/s/ldl0tjd2q41soa3ckqrmfp3wb38q2z19)

#### Evaluation

I use three evaluation methods, combining quantitative and qualitative approaches.

The baseline NER labels randomly tags 7% of all texts as Named Entities (see `baselineBERT.ipynb` for citation from a research that identifies 7% as the average proportion of Named Entities in texts).

I have three evaluation methods (you can see them in the file `evaluation.ipynb` in the `notebooks` directory): number of labels, consistency in labels, and qualitative human examination. During evaluation, since I'm working with a dataset that is underutilized, there does not exist a ground truth human NER labeling for these newspaper pages that I'm working with. So, I'm using the labeling result of a reputable NER tool (Stanford NER) and treat Stanford NER's labels as the "gold" standard and see if my fine-tuned model performs as good as the Stanford NER model on these NER labeling tasks.

You can see details of the evaluation and critical reflection and analysis in the `evaluation.ipynb` file. For a quick summary: 

- Both my model and Stanford NER labeled mess than 7% of words (baseline) as Named Entites. This is expected because I am only looking at three NER categories (Person, Organization, and Organiztion). However, Stanford NER outperforms my model because Stanford NER labeled 3.5%, which is about half of the baseline, and this matches with the reduced NER count because Person, Organization, and Organiztion are three major NER categories, and by including just the three of them, we can account for a good percentage of all Named Entites. My model, on the other hand, only labeled 0.5% of words. This is below the accepted range of labels. Meaning, Stanford NER saw more labels than my model.
    - This means that my model has low `recall` score.
- When it comes to consistency in NER labeling (a metric to see if a Named Entity is labeled to the same category when used in different context. This builds on the assumption that a Named Entity, because of its nature, does not change meaning or connotation in different context), my model and the Stanford NER model perform similarly, where in the four scenarios that I'm testing, my model outperforms Stanford NER in two of them.
- With qualitative analysis, I randomly selected 3 NER labels each from 100 randomly selected newspaper pages. By examining the labels created by my model, I believe that my model has done a decent enough job at labeling named entities for writing from a time period that the model is not fine-tuned on. My model could understand complex abbreviations (like "N.M" is a LOCATION because it refers to New Mexico). Although my model is not perfect, it demonstrated a high `precision`.

Judging from the 3 evaluation methods, my model is accurate enough at the Named Entities that it has identified, but it is not as good at finding Named Entities.


#### Individual contribution:

This is a solo project. All work was done by me.
