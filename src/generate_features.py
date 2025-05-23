from haar_feature import HaarFeature

def generate_features(window_size = 24):
    features = []
    
    for feature_type in ['two-rectangle-horizontal','two-rectangle-vertical','three-rectangle-horizontal','three-rectangle-vertical','four-rectangle']:
        for w in range (1, window_size + 1):
            for h in range(1, window_size + 1):
                for x in range(0, window_size - w + 1):
                    for y in range(0, window_size - h + 1):
                        feature = HaarFeature(feature_type, (x, y), w, h)
                        features.append(feature)
    return features