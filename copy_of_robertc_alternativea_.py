# -*- coding: utf-8 -*-
"""Copy of RobertC-AlternativeA_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TQ2S0byblHi52AoGf62Hbi_GTE92qk-5
"""

import pandas as pd
import math

#create a dataframe for our alternative analysis matrix
AA=pd.DataFrame(columns=['criteria','weight','ratingA','ratingB','scoreA','scoreB'])
print(AA)

# First step: add a list of criteria
AA['criteria']=['risk', 'ROI', 'customerSatisfaction', 'feasibility','strategicAlignment']
print(AA)

# second step: identify weights
# weights show relatve importance of each criterion
# they must add up to 1 (or 100 if you use percentage)

AA['weight']=[0.1,0.15,0.3,.15,.3]
print(AA)

# step 3: rate each alternative across all criteria
# choose a scale: 1-5 or 1-7 or 1-10, or 1-3
# higher number: an alternative is doing better with respect to  that specific criterion

AA['ratingA']=[4,1,2,1,5]
AA['ratingB']=[3,4,2,3,2]

#step 4: calculate partial scores by multiplying weights * ratings
for index, row in AA.iterrows():
  AA['scoreA'][index]=row['ratingA']*row['weight']
  AA['scoreB'][index]=row['ratingB']*row['weight']

print(AA)

#Step 5: add partial scores to get the total scores
#which solution is the winner? the one with the highest total score
totalScoreA=0
totalScoreB=0
for index, row in AA.iterrows():
  totalScoreA+=row['scoreA']
  totalScoreB+=row['scoreB']

print('total score for A is {:.2f} and for B is {:.2f}'.format(totalScoreA, totalScoreB))

# step 5: add partial scores to get the total scores
# the solution with the highest score is the winner
totalScoreA=0
totalScoreB=0
for index, row in AA.iterrows():
  totalScoreA+=row['scoreA']
  totalScoreB+=row['scoreB']

print ('the total score for alternative A is {:.2f} and for B is {:.2f}'.format(totalScoreA, totalScoreB))

import numpy as np
import matplotlib.pyplot as plt

axisLocations = np.linspace(start=0, stop=2 * np.pi, num=len(AA['ratingA']), endpoint=False)
axisLocations = np.concatenate((axisLocations,[axisLocations[0]]))
ratingsA=AA['ratingA']
ratingsB=AA['ratingB']
ratingsACircular=np.concatenate((ratingsA,[ratingsA[0]]))
ratingsBCircular=np.concatenate((ratingsB,[ratingsB[0]]))

plt.figure(figsize=(8,8))
plt.subplot(polar=True)
plt.plot(axisLocations, ratingsACircular, 'o-', linewidth=2, label='In-house development')
plt.plot(axisLocations, ratingsBCircular, 'd-', linewidth=2, label='Outsource')
#plt.plot(label_loc, resaurant_3, label='Restaurant 3')
plt.title('Project Options Comparisons', size=20)
lines, labels = plt.thetagrids(np.degrees(axisLocations), labels=AA['criteria'])
plt.legend()
plt.show()