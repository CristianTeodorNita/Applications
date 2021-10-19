'''
This little app reads data from a csv regarding (here is used as an example a csv name music.csv that is in the folder)
First you have to install the pandas module, open command prompt and use: pip install pandas
Second you need to install the sklearn module, open command promt and use : pip install -U scikit-learn
.dot file is opened in VSCode
'''
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# from sklearn.externals import joblib
from sklearn import tree


music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X, y)
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)

# joblib.dump(model, 'music-recommeder.joblib')
# joblib.load('music-recommeder.joblib')

tree.export_graphviz(model, out_file='music-recommeder..dot',
                     feature_names=['age', 'gender'],
                     class_names=sorted(y.unique()),
                     label='all',
                     rounded=True,
                     filled=True)

# predictions = model.predict([[21, 1]])
# predictions
# score = accuracy_score(y_test, predictions)

