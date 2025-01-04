def unique_labels(labels: list) -> dict:
    rst = {}
    for label in labels:
        if label not in rst.keys():
            rst[label] = 0
        else:
            rst[label] += 1

    return rst
