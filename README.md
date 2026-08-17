# Language Identification Model Results:

## Validation accuracy: 98.35%
```
              precision    recall  f1-score   support

      Arabic       1.00      1.00      1.00        89
     Chinese       0.98      0.99      0.98        92
       Dutch       1.00      1.00      1.00        85
     English       0.81      1.00      0.89        96
    Estonian       1.00      0.95      0.97        96
      French       0.98      1.00      0.99       101
       Hindi       1.00      0.97      0.99        79
  Indonesian       1.00      0.93      0.97        89
    Japanese       1.00      0.99      0.99        91
      Korean       1.00      0.98      0.99        97
       Latin       0.97      0.98      0.97        89
     Persian       1.00      1.00      1.00        97
   Portugese       0.99      0.99      0.99        77
      Pushto       1.00      0.96      0.98        89
    Romanian       1.00      0.99      0.99        92
     Russian       0.98      1.00      0.99        84
     Spanish       1.00      0.97      0.98        89
     Swedish       1.00      1.00      1.00        97
       Tamil       1.00      0.99      0.99       100
        Thai       1.00      0.98      0.99        96
     Turkish       1.00      0.99      0.99        81
        Urdu       1.00      0.99      0.99        94

    accuracy                           0.98      2000
   macro avg       0.99      0.98      0.98      2000
weighted avg       0.99      0.98      0.98      2000
```
## Terms:
- Precision: How correct the prediction is.
- Recall: Of all the samples of a given language, how many did the model actually find?
- F1-score: A ratio of the recall and precision.
- Support: How much of a given language was included in the validation data.

## Validation Confusion Matrix
### How to read:
1) Pick any box on the grid
2) Look at the row and a column
3) Row is the actual language, column is the predicted
4) This shows what the model confused what for what

<img width="1276" height="1260" alt="image" src="https://github.com/user-attachments/assets/8df1647f-1a99-45e6-8580-1dccf44b6ddb" />

## Dataset Used:
https://www.kaggle.com/datasets/zarajamshaid/language-identification-datasst
