def minMaxScale(data):
    for feature in data.columns:
        data[feature] = (data[feature] - data[feature].min()) / (data[feature].max() - data[feature].min())
    return data


def standardizationScale(data):
    for feature in data.columns:
        exp = data[feature].mean()
        div = data[feature].std()
        data[feature] = (data[feature] - -exp) / (div)
    return data
