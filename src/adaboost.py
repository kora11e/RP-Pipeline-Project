import numpy as np
from weak_classifier import WeakClassifier

class AdaBoost:
    def __init__(self, num_classifiers):
        self.num_classifiers = num_classifiers
        self.strong_classifier = []

    def train(self, training_data, labels, features):
        num_samples = len(training_data)
        weights = np.ones(num_samples) / num_samples

        for _ in range(self.num_classifiers):
            best_classifier = None
            best_error = float('inf')
            best_pred = None

            for feature in features:
                values = [feature.compute_value(img) for img in training_data]
                thresholds = np.linspace(min(values), max(values), 10)
                for threshold in thresholds: 
                    for polarity in [1, -1]:
                        classifier = WeakClassifier(feature, threshold, polarity)
                        predictions = np.array([classifier.predict(img) for img in training_data])
                        if np.any(predictions == None):
                            continue
                        error = np.sum(weights * (predictions != labels))
                        if error < best_error:
                            best_error = error
                            best_classifier = classifier
                            best_pred = predictions
            if best_classifier is None or best_pred is None:
                continue
            epsilon = 1e-10
            alpha = 0.5 * np.log((1 - best_error) / (best_error + epsilon))
            weights *= np.exp(-alpha * labels * (2 * best_pred - 1))
            weights /= np.sum(weights)

            self.strong_classifier.append((alpha, best_classifier))

    def predict(self, integral_img):
        total = sum(alpha * (2 * clf.predict(integral_img) - 1)
                    for alpha, clf in self.strong_classifier)
        return 1 if total >= 0 else 0