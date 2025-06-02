class WeakClassifier:
    def __init__(self, feature, threshold, polarity):
        self.feature = feature
        self.threshold = threshold
        self.polarity = polarity

    def predict(self, integral_img):
        feature_value = self.feature.compute_value(integral_img)
        return 1 if self.polarity * feature_value < self.polarity * self.threshold else 0