import seaborn as sns
import matplotlib.pyplot as plt
import math
# income = [-5,-4,-2,-1,0,2,3,4,5]
# loan = [0,0,0,0,0,1,1,1,1]
#
# sns.scatterplot(x=income,y=loan)
# plt.show()

def logf(x):
    res = 1/(1+math.exp(-x))
    return res
