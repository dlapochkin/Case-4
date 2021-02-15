
training = input()
from textblob import classifiers
classifier = classifiers.NaiveBayesClassifier(training)
print(training)
