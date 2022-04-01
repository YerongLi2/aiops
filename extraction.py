from rake_nltk import Rake
import pandas as pd
r = Rake()

df = pd.read_csv('cuda.csv')
posts = eval(df.loc[0].posts)
text = posts[0][0]

print(text)
print(r.extract_keywords_from_text(text))