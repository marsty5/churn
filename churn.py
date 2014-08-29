import pandas as pd
import numpy as np
from create_tree import create_tree

customerDf = pd.read_csv('datasets/churn.data.simple.noDot')
del customerDf['state']
del customerDf['area_code']
del customerDf['international_plan']
del customerDf['voice_mail_plan']

create_tree(customerDf)
