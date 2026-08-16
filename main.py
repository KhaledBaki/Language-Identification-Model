# ============================================================
# Khaled Abdul-Baki
# August 15, 2026
# ============================================================

# Required libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from matplotlib import pyplot as plt # For graph plotting
from sklearn.feature_extraction.text import TfidfVectorizer as vect # Vectorize the strings
from sklearn.linear_model import LogisticRegression # For logistic regression
from sklearn.metrics import accuracy_score, classification_report # To get the report of the model


# Reading data from csv 
data = pd.read_csv('/kaggle/input/datasets/zarajamshaid/language-identification-datasst/dataset.csv')
data = np.array(data)
m,n = data.shape
print("Rows: " + str(m) + ", Columns: " + str(n)) # Rows and Columns


# Shuffle dataset
np.random.shuffle(data)

# Preserved validation  9.09% of dataset size
validationData = data[0:2000]

# Training data
trainingData = data[2000: m]


# Splitting the two columns we have: Column 0 -> Text, Column 1 -> Label

# Training Set
X_Training_Data_Text = trainingData[:,0]
Y_Training_Data_Label = trainingData[:,1]

# Validation Set
X_Validation_Text = validationData[:,0]
Y_Validation_Label = validationData[:,1]

# Verifying size properties
print(X_Training_Data_Text.shape)
print(Y_Training_Data_Label.shape)

print(X_Validation_Text.shape)
print(Y_Validation_Label.shape)


# Vectorizing the input 
vectorizer = vect(
    
    # Spliting the text by character
    analyzer="char",

    # Extract sequences 2 to 5 characters long
    ngram_range=(2, 5),

    # Minimun document frequency -> any character sequence that appears less than two times is ignored
    # Basically meaning noise cleaning
    min_df=2,

    # Applying logarithmic weighting to the term frequency -> (1 + log(termFrequency))
    sublinear_tf=True
)


# Fit and transform the data
trainXData = vectorizer.fit_transform(X_Training_Data_Text)

# Convert it to sparse matrix i.e. mostly zeros -> saves memory and computation
# Tf-idf-weighted document-term matrix.
validateXData = vectorizer.transform(X_Validation_Text)


model = LogisticRegression(

    # Maximum number of iterations taken for the solvers to converge
    max_iter=1000,

    # Specific optimization algorithm, same idea as using gradient descent
    solver="saga",
    
    n_jobs=-1
)


# Training the model with the learn library
model.fit(trainXData, Y_Training_Data_Label)

# Get prediction
prediction = model.predict(validateXData)

# Get accuracy
accuracy = accuracy_score(Y_Validation_Label, prediction)

# Output the report details
print(f"Validation accuracy: {accuracy:.2%}")
print(classification_report(Y_Validation_Label, prediction))
