import pandas as pd

customerDf = pd.read_csv('datasets/churn.data.simple.noDot')

# Create the decision tree model
def create_tree(customerDf):

    attributes = customerDf.columns
    information_gains = map(lambda x: information_gain(x,customerDf),attributes)


# Calculate the information gain of one attribute
def information_gain(attribute, customerDf):
    # TODO
    return 0.0




