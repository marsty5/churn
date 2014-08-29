from calc_info_gain import information_gain

def create_tree(df):

    return split(df)

def split(df):

    if len(df)==0:
        return []
    attributes = df.columns.drop('churn')
    if len(attributes)==0: 
        return []

    #print len(df)
    information_gains = map(lambda x: information_gain(x,df),attributes)

    idx = information_gains.index(max(information_gains))
    best_attribute = attributes[idx]
    
    att_mean = df[best_attribute].mean()
    filteredDfLeft = df[df[best_attribute]<att_mean]
    filteredDfRight = df[df[best_attribute]>=att_mean]

    if len(attributes)==1:
        final_values = []
        if len(filteredDfLeft[best_attribute])!=0:
            att_mean = filteredDfLeft[best_attribute].mean()
            numbers = filteredDfLeft[filteredDfLeft[best_attribute] < att_mean].groupby('churn')[best_attribute].count()
            true_values = 0
            false_values = 0
            if ' True' in numbers:
                true_values = numbers[' True']
            if ' False' in numbers:
                false_values = numbers[' False']
            if true_values > false_values:
                final_values = ['True']
            else:
                final_values = ['False']
        
        if len(filteredDfRight[best_attribute]!=0):
            att_mean = filteredDfRight[best_attribute].mean()
            numbers = filteredDfRight[filteredDfRight[best_attribute] < att_mean].groupby('churn')[best_attribute].count()
            true_values = 0
            false_values = 0
            if ' True' in numbers:
                true_values = numbers[' True']
            if ' False' in numbers:
                false_values = numbers[' False']
            if true_values > false_values:
                final_values = final_values + ['True']
            else:
                final_values = final_values + ['False']

        return final_values
    
    del filteredDfLeft[best_attribute]
    del filteredDfRight[best_attribute]

    return [best_attribute] + split(filteredDfLeft) + split(filteredDfRight)
    #return best_attribute

