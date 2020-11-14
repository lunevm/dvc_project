import pandas as pd

df = pd.DataFrame({'a': range(10000), 'b': range(0, -10000, -1)})

df.to_csv('data/df.csv')