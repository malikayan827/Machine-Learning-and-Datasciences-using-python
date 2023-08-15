import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# Call the load_digits function to actually load the dataset
digits = load_digits()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data,
                                                    digits.target,
                                                    test_size=0.2)
len(X_train), len(X_test)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)
plt.matshow(digits.images[67])
plt.show()
print(digits.target[67])

# print(model.predict([digits.data[67]]))
#chechking the accuracy of the model
y_predicted = model.predict(X_test)
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_predicted)
import seaborn as sn
plt.figure(figsize=(10, 7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()

