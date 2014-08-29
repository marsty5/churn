import math

# Calculate the information gain of one attribute
def information_gain(attribute, customerDF):
    # TODO
    #   x = #churned/#entries
    #   y = #!churned/#entries 
    #   Calculate parent_entropy: (-x * log x) + (-y * log y)
    if ( ' True' in customerDF.groupby('churn')[attribute].count()):
      att_churned = float(customerDF.groupby('churn')[attribute].count()[' True']) / customerDF[attribute].count()
    else:
      att_churned = 0
    if ( ' False' in customerDF.groupby('churn')[attribute].count()): 
      att_non_churned = float(customerDF.groupby('churn')[attribute].count()[' False']) / customerDF[attribute].count()
    else:
      att_non_churned = 0
    if ( att_churned == 0 ):
      att_churned_part = 0
    else:
      att_churned_part = -att_churned * math.log( att_churned )
    if ( att_non_churned == 0):
      att_non_churned_part = 0
    else:
      att_non_churned_part = -att_non_churned * math.log( att_non_churned )
    parent_entropy = att_churned_part + att_non_churned_part
    #   Calculate average and split in two categories (<average, >=average
    #   x1 = #churned / #entries1 (< average)
    #   y1 = #!churned/ #entries1 (< average)
    #   x2 = #churned / #entries2 (>= average)
    #   y2 = #!churned/ #entries2 (>= average)
    att_mean = customerDF[attribute].mean()
    att_mean_less = customerDF[customerDF[attribute] < att_mean][attribute].count()
    if ( ' True' in customerDF[customerDF[attribute] < att_mean].groupby('churn')[attribute].count()):
      att_mean_less_churned = float(customerDF[customerDF[attribute] < att_mean].groupby('churn')[attribute].count()[' True']) / att_mean_less
    else:
      att_mean_less_churned = 0
    if ( ' False' in customerDF[customerDF[attribute] < att_mean].groupby('churn')[attribute].count()):
      att_mean_less_non_churned = float(customerDF[customerDF[attribute] < att_mean].groupby('churn')[attribute].count()[' False']) / att_mean_less
    else:
      att_mean_less_non_churned = 0
    att_mean_more = customerDF[customerDF[attribute] >= att_mean][attribute].count()
    if ( ' True' in customerDF[customerDF[attribute] >= att_mean].groupby('churn')[attribute].count()):
      att_mean_more_churned = float(customerDF[customerDF[attribute] >= att_mean].groupby('churn')[attribute].count()[' True']) / att_mean_more
    else:
      att_mean_more_churned = 0
    if ( ' False' in customerDF[customerDF[attribute] >= att_mean].groupby('churn')[attribute].count()):
      att_mean_more_non_churned = float(customerDF[customerDF[attribute] >= att_mean].groupby('churn')[attribute].count()[' False']) / att_mean_more
    else:
      att_mean_more_non_churned = 0
    #   child_entropy_1: (-x1 * log x1) + (-y1 * log y1)
    #   child_entropy_2: (-x2 * log x2) + (-y2 * log y2)
    #   avg_child_entropy = (child_entropy_1 + child_entropy_2) / 2
    if ( att_mean_less_churned == 0 ):
      att_mean_less_churned_part = 0
    else:
      att_mean_less_churned_part = -att_mean_less_churned * math.log( att_mean_less_churned )
    if ( att_mean_less_non_churned == 0 ):
      att_mean_less_non_churned_part = 0
    else:
      att_mean_less_non_churned_part = -att_mean_less_non_churned * math.log( att_mean_less_non_churned )
    child_entropy_less = att_mean_less_churned_part + att_mean_less_non_churned_part
    
    if ( att_mean_more_churned == 0 ):
      att_mean_more_churned_part = 0
    else:
      att_mean_more_churned_part = -att_mean_more_churned * math.log( att_mean_more_churned )
    if ( att_mean_more_non_churned == 0 ):
      att_mean_more_non_churned_part = 0
    else:
      att_mean_more_non_churned_part = -att_mean_more_non_churned * math.log( att_mean_more_non_churned )
    
    child_entropy_less = att_mean_less_churned_part + att_mean_less_non_churned_part
    child_entropy_more = att_mean_more_churned_part + att_mean_more_non_churned_part

    #   information_gain = parent_entorpy - avg_child_entropy
    info_gain = parent_entropy - ( float((child_entropy_less + child_entropy_more)) / 2 )
    return info_gain

