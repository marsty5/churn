from calc_info_gain import information_gain

def create_tree(df):

    return split(df)

def split(df):

    if len(df)==0:
        return []
    attributes = df.columns.drop('churn')
    if len(attributes)==0: 
        return []

    information_gains = map(lambda x: information_gain(x,df),attributes)

    idx = information_gains.index(max(information_gains))
    best_attribute = attributes[idx]
    
    att_mean = df[best_attribute].mean()
    filteredDfLeft = df[df[best_attribute]<att_mean]
    filteredDfRight = df[df[best_attribute]>=att_mean]
    del filteredDfLeft[best_attribute]
    del filteredDfRight[best_attribute]

    return [best_attribute] + split(filteredDfLeft) + split(filteredDfRight)

