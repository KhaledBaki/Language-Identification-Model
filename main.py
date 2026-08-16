# ============================================================
# Khaled Abdul-Baki
# August 15, 2026
# ============================================================
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from matplotlib import pyplot as plt


# Reading data from csv 
data = pd.read_csv('/kaggle/input/datasets/zarajamshaid/language-identification-datasst/dataset.csv')
data = np.array(data)
m,n = data.shape

# Rows and Columns
print("Rows: " + str(m) + ", Columns: " + str(n))


# Shuffle dataset
np.random.shuffle(data)

# Preserved validation data
validationData = data[0:2000]

# Training data
trainingData = data[2000: m]
