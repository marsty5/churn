from calc_info_gain import information_gain

#Create the decision tree model
def create_tree(customerDf):
  attributes = customerDf.columns.drop('churn')
  information_gains = map(lambda x: information_gain(x,customerDf),attributes)
  print information_gains
  return 0.0

