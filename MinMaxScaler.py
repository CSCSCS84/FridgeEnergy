def scale(data):
    for feature in data.columns:
        data[feature] = (data[feature] - data[feature].min()) / (data[feature].max() - data[feature].min())
    return data