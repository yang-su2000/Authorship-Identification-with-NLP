import pandas as pd
import numpy as np
f = open("author_features.txt","r")

lines = f.readlines()
author = []
affiliation = []
for line in lines:
    author.append(line.split(",", 1)[0])
    affiliation.append(line.split(",", 1)[1])

data = np.array([author, affiliation]).T
print(data.shape)
pd.DataFrame(data, columns=["authors","affiliation"]).to_csv("author_and_features.csv")