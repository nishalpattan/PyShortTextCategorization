from collections import defaultdict
import json

import pandas as pd


def retrieve_csvdata_as_dict(filepath):
    """ Retrieve the training data in a CSV file.

    Retrieve the training data in a CSV file, with the first column being the
    class labels, and second column the text data. It returns a dictionary with
    the class labels as keys, and a list of short texts as the value for each key.

    :param filepath: path of the training data (CSV)
    :return: a dictionary with class labels as keys, and lists of short texts
    :type filepath: str
    :rtype: dict
    """
    df = pd.read_csv(filepath)
    category_col, descp_col = df.columns.values.tolist()
    shorttextdict = defaultdict(lambda : [])
    for category, descp in zip(df[category_col], df[descp_col]):
        shorttextdict[category] += [descp]
    return dict(shorttextdict)

# for backward compatibility
def retrieve_data_as_dict(filepath):
    """ Retrieve the training data in a CSV file.

    This calls :func:`~retrieve_csvdata_as_dict` for backward compatibility.

    :param filepath: path of the training data (CSV)
    :return: a dictionary with class labels as keys, and lists of short texts
    :type filepath: str
    :rtype: dict
    """
    return retrieve_csvdata_as_dict(filepath)

def retrieve_jsondata_as_dict(filepath):
    """ Retrieve the training data in a JSON file.

    Retrieve the training data in a JSON file, with
    the class labels as keys, and a list of short texts as the value for each key.
    It returns the corresponding dictionary.

    :param filepath: path of the training data (JSON)
    :return: a dictionary with class labels as keys, and lists of short texts
    :type filepath: str
    :rtype: dict
    """
    return json.load(open(filepath, 'r'))