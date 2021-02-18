import pandas as pd
import re
from nltk import word_tokenize
from nltk.corpus import stopwords

stop_words = stopwords.words("english")

url_regex_pattern = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
def clean_data(tweet_text):
	#tweet_text = tweet_text.lower()
	tweet_text = re.sub(r'RT\s@\w+:','',tweet_text)
	tweet_text = re.sub(r'@\w+','',tweet_text)
	tweet_text = re.sub(url_regex_pattern,'',tweet_text)

	tweet_text = word_tokenize(tweet_text)
	tweet_cleaned = []
	for word in tweet_text:
		if word.isalpha() and word not in stop_words:
			tweet_cleaned.append(word.lower())

	return " ".join(tweet_cleaned)



df = pd.read_csv("tweets.csv",encoding="utf-8")
print(df.shape)


print("Before:", df.iloc[23]["text"])
df["text"] = df["text"].apply(clean_data)
print("After:", df.iloc[23]["text"])


df.to_csv("data_cleaned.csv",index=None)


from wordcloud import WordCloud

import matplotlib.pyplot as plt

wordcloud = WordCloud(background_color="black").generate(str(df["text"].values))

plt.imshow(wordcloud)

plt.show()
