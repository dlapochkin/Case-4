from textblob import classifiers
training = input()
classifier = classifiers.NaiveBayesClassifier(training)
print(classifier)
