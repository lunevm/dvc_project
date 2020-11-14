import pandas as pd

df = pd.DataFrame({'a': range(1000), 'b': range(0, -1000, -1)})

df.to_csv('data/df.csv')