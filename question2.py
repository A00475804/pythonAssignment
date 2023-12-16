# -*- coding: utf-8 -*-
"""

@author: mehta
"""

import pandas as pd;

df = pd.read_csv("imdb.csv", usecols=['title'])
print(df)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

df['Vowels'] = df['title'].apply(count_vowels)

print(df)