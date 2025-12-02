## Attribution
The code in this project was created from a combination of multiple sources:

- My own code.
- CS 372 HW 5 Notebook 1: I used both my own answer response for this NB and the code provided for us in this NB for portions of my BERT fine-tuning process (file `FineTuneBERT.ipynb`).
- CS 372 HW 4 Notebook 1: I used the function `plot_training_curves` provided there to plot my training loss and validation score curves during my BERT fine-tuning process (file `FineTuneBERT.ipynb`).
- Library of Congress <i>Chronicling America</i> API documentation [link](https://libraryofcongress.github.io/data-exploration/loc.gov%20JSON%20API/Chronicling_America/ChronAm_analyzing_specific_titles_limit_results.html): I used code provided in this documentation for the API access pipeline in the file `LibraryOfCongressDocumentExtraction.ipynb`.
- CS 101 Assignment 5 Fall 2025 Set Up Code: For my pipeline in calling DukeAI's API Gateway to clean messy OCR from Chronicling America, I borrowed the API call structure used in CS 101 Assignment 5 here [link](https://courses.cs.duke.edu/fall25/compsci101/wordgames/assign/wordgame.html#appendix-optional-generating-hints-with-dukegpthints-py). I revised the structure significantly to fit my context.
- Duke Compute Cluster documentation [link](https://dcc.duke.edu/dcc/): I used the SLURM and Bash code provided in the DCC documentation to speed up the process of accessing Chronicling America API. The code is used in the directory `DCCMistral`.
- Claude Sonnet 4.5 free version: I used this AI tool to debug my code and write helper functions. See comments in individual code cells or files for my specific usages. In summary, I used Claude to create reusable functions in `runFineTunedBERT.ipynb` and `FineTuneBERT.ipynb`.