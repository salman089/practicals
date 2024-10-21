"""pr.8 #AIM: Implement AdaBoost(Adaptive Boosting) learning algorithm."""


import pandas as pd  # Import pandas for data manipulation
from sklearn import model_selection  # Import model_selection for cross-validation
from sklearn.ensemble import AdaBoostClassifier  # Import the AdaBoost classifier

# Load the dataset from a URL
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']  # Column names
dataframe = pd.read_csv(url, names=names)  # Read the CSV file into a pandas DataFrame

# Prepare the data
array = dataframe.values  # Convert the DataFrame into a NumPy array
X = array[:, 0:8]  # Feature variables (first 8 columns)
Y = array[:, 8]    # Target variable (last column)

# Set seed for reproducibility and specify number of trees in AdaBoost
seed = 7
num_trees = 30

# Create the AdaBoost classifier using the SAMME algorithm
model = AdaBoostClassifier(n_estimators=num_trees, algorithm='SAMME', random_state=seed)

# Evaluate the model using cross-validation
results = model_selection.cross_val_score(model, X, Y)

# Print the mean accuracy of the model
print("Mean Accuracy:", results.mean())
