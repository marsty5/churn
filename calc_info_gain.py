import math

# Calculate the information gain of one attribute
def information_gain(attribute, customerDF):
    # TODO
    #   x = #churned/#entries
    #   y = #!churned/#entries 
    #   Calculate parent_entropy: (-x * log x) + (-y * log y)
    att_churned = float(customerDF.groupby('churn')[attribute].count()[1]) / customerDF[attribute].count()
    att_non_churned = float(customerDF.groupby('churn')[attribute].count()[0]) / customerDF[attribute].count()
    parent_entropy = -att_churned * math.log( att_churned ) + (-att_non_churned * math.log( att_non_churned ) )
    #   Calculate average and split in two categories (<average, >=average
    #   x1 = #churned / #entries1 (< average)
    #   y1 = #!churned/ #entries1 (< average)
    #   x2 = #churned / #entries2 (>= average)
    #   y2 = #!churned/ #entries2 (>= average)
    att_mean = customerDF[attribute].mean()
    att_mean_less = customerDF[customerDF[attribute] < att_mean][attribute].count()
    att_mean_less_churned = float(customerDF[customerDF[attribute] < att_mean].groupby('churn')[attribute].count()[1]) / att_mean_less
    att_mean_less_non_churned = float(customerDF[customerDF[attribute] < att_mean].groupby('churn')[attribute].count()[0]) / att_mean_less

    att_mean_more = customerDF[customerDF[attribute] >= att_mean][attribute].count()
    att_mean_more_churned = float(customerDF[customerDF[attribute] >= att_mean].groupby('churn')[attribute].count()[1]) / att_mean_more
    att_mean_more_non_churned = float(customerDF[customerDF[attribute] >= att_mean].groupby('churn')[attribute].count()[0]) / att_mean_more

    #   child_entropy_1: (-x1 * log x1) + (-y1 * log y1)
    #   child_entropy_2: (-x2 * log x2) + (-y2 * log y2)
    #   avg_child_entropy = (child_entropy_1 + child_entropy_2) / 2
    child_entropy_less = -att_mean_less_churned * math.log( att_mean_less_churned ) + ( -att_mean_less_non_churned * math.log( att_mean_less_non_churned ) )
    child_entropy_more = -att_mean_more_churned * math.log( att_mean_more_churned ) + ( -att_mean_more_non_churned * math.log( att_mean_more_non_churned ) )

    #   information_gain = parent_entorpy - avg_child_entropy
    info_gain = parent_entropy - ( float((child_entropy_less + child_entropy_more)) / 2 )
    return info_gain

