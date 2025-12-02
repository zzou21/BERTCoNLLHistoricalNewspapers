This Markdown file reports on my comparison for using different hyperparameters during BERT fine-tuning:

Since I used multiple sets of hyperparameters to compare the performance of my BERT fine-tuning process, I'm comparing them to each other and see, for four hyperparameters, which hyperparameter setup is the most suitable for fine-tuning a BERT model on the CoNLL 2003 database. I'm using five sets pf hyperparameters, and you can find the training code in the `FineTuneBERT.ipynb` notebook.

<b>Final result:</b> Hyperparameter set 1 is the best.

<b>Set 1:</b>
- learning rate: 0.00001
- batch size: 8
- epoch: 7
- early stopping patience: 2

1. Result: no early stopping. Used all training epochs.
2. Best training loss: 0.0051
3. Best validation accuracy: 99.16% 

<b>Set 2:</b>
- learning rate: 0.00006
- batch size: 8
- epoch: 6
- early stopping patience: 2

1. Result: early stopping at 5th epoch.
2. Best training loss: 0.019
3. Best validation accuracy: 98.8% 


<b>Set 3:</b>
- learning rate: 0.00009
- batch size: 10
- epoch: 6
- early stopping patience: 2

1. Result: early stopping at 3rd epoch.
2. Best training loss: 0.046
3. Best validation accuracy: 98.6% 


<b>Set 4:</b>
- learning rate: 0.000005
- batch size: 10
- epoch: 10
- early stopping patience: 2

1. Result: early stopping at 7th epoch.
2. Best training loss: 0.0098
3. Best validation accuracy: 99.1% 

<b>Set 5:</b>
- learning rate: 0.000005
- batch size: 8
- epoch: 10
- early stopping patience: 3

1. Result: early stopping at 4th epoch.
2. Best training loss: 0.0056
3. Best validation accuracy: 99.05% 
