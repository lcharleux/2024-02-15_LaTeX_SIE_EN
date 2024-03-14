import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/data.csv')

output = data.describe().to_latex()
with open('table1.tex', 'w') as f:
    f.write(output)