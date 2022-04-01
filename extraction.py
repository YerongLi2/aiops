from rake_nltk import Rake
import pandas as pd
r = Rake()

df = pd.read_csv('cuda.csv')
posts = eval(df.loc[0].posts)
text = posts[0][0]

print('text')
print(text)
r.extract_keywords_from_text(text)
print(r.get_ranked_phrases_with_scores)