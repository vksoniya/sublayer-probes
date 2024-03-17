
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split

import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

# Create a OneVsRestClassifier using LogisticRegression as the base classifier
def train_predict_onevsrest_linearclassifier(sublayerembeddings, layer_num, labels):
	clf = OneVsRestClassifier(LogisticRegression(random_state=42))

	# Split the data into training and testing sets (adjust the test_size as needed)
	X_train, X_test, y_train, y_test = train_test_split(sublayerembeddings, labels, test_size=0.4, random_state=42)


	# Train the classifier on the training data
	clf.fit(X_train, y_train)

	# Make predictions on the testing data
	y_pred = clf.predict(X_test)
	#print(y_test)
	#print(y_pred)
	# Evaluate the performance of the classifier (using appropriate metrics)
	accuracy = accuracy_score(y_test, y_pred)
	f1 = f1_score(y_test, y_pred, average='micro')  # Consider different averaging strategies for F1
	#print("Layer number: ", layer_num)
	#print("Accuracy:", accuracy)
	print(accuracy)
	#print("F1 Score:", f1)


def train_svm_linearclassifier(sublayerembeddings, layer_num, labels):
	# Split the data into training and testing sets (adjust the test_size as needed)
	X_train, X_test, y_train, y_test = train_test_split(sublayerembeddings, labels, test_size=0.2, random_state=42)

	# Create an SVM classifier with a linear kernel (adjust kernel or other hyperparameters if needed)
	clf = svm.SVC(kernel='linear')

	# Train the classifier on the training data
	clf.fit(X_train, y_train)

	# Make predictions on the testing data
	y_pred = clf.predict(X_test)

	# Evaluate the performance of the classifier (adjust evaluation metrics as needed)
	from sklearn.metrics import accuracy_score
	accuracy = accuracy_score(y_test, y_pred)
	print("Layer number: ", layer_num)
	print("Accuracy:", accuracy)
	print(accuracy)
