from rake_ntlk import Rake
import pandas as pd
r = Rake()

df = pd.read_csv('cuda.csv')
posts = eval(df.loc[0])

print(posts)