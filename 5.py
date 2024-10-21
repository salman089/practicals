"""P5: Implement Decision-Tree learning algorithm.
The objective of this experiment is to implement the Decision Tree Learning algorithm using a dataset, build a decision tree,
evaluate the accuracy and effectiveness of the model on test data, and visualize the resulting tree. 
Decision trees are widely used for classification tasks because of their simplicity and interpretability.

pip install pandas scikit-learn matplotlib
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('dataset.csv')
X = data.drop('target', axis=1)  # Features
y = data['target']  # Target variable

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Evaluate model
accuracy = model.score(X_test, y_test)
print(f'Accuracy: {accuracy:.2f}')

# Visualize tree
plt.figure(figsize=(12, 8))
plot_tree(model, filled=True)
plt.title('Decision Tree')
plt.show()
