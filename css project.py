# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:30:01 2024

@author: HomePC
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

df = pd.read_csv("C:/Users/HomePC/Desktop/Desktop/movie_dataset.csv")

print(df.columns)


print("QUESTION 1")
#mean before filling in nan values
initial_mean = df['Revenue (Millions)'].mean()
print(initial_mean)

#filling in nan values
df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].mean(), inplace=True)
print(df)

df['Metascore'].fillna(df['Metascore'].mean(), inplace=True)
print(df)

#new mean after filling in nan values
new_mean = df['Revenue (Millions)'].mean()
print(new_mean)

print("\nQUESTION 3")
# Filter the dataframe for movies released between 2015 and 2017
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Calculate the average revenue for the filtered movies
average_revenue_2015_2017 = filtered_df['Revenue (Millions)'].mean()
print(average_revenue_2015_2017)

print("\nQUESTION 4")
# Filter the dataframe for movies released in 2016
movies_2016 = df[df['Year'] == 2016]

# Count the number of movies released in 2016
num_movies_2016 = len(movies_2016)
print(num_movies_2016)

print("\nQUESTION 5")
# To find the number of movies directed by Christopher Nolan
num_movies_nolan_directed = df[df['Director'] == 'Christopher Nolan'].shape[0]

print(num_movies_nolan_directed)

print("\nQUESTION 6")
# Count the number of movies with a rating of at least 8.0
num_high_rated_movies = df[df['Rating'] >= 8.0].shape[0]
print(num_high_rated_movies)

#QUESTION 7
print("\nQUESTION 7")
# Filter the dataframe for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median rating of movies directed by Christopher Nolan
median_rating_nolan_directed = nolan_movies['Rating'].median()
print(median_rating_nolan_directed)

#QUESTION 8
print("\nQUESTION 8")
# Calculate the average rating for each year and find the year with the highest average rating
yearly_average_rating = df.groupby('Year')['Rating'].mean()
year_with_highest_rating = yearly_average_rating.idxmax()

print('\nQ8')
print(year_with_highest_rating)

#QUESTION 9
# Count the number of movies made in 2006
num_movies_2006 = df[df['Year'] == 2006].shape[0]

# Count the number of movies made in 2016
num_movies_2016 = df[df['Year'] == 2016].shape[0]

# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

print('\nQUESTION 9')
print(percentage_increase)

#QUESTION 10
# Combine all the actor names into a single list
all_actors = df['Actors'].str.split(', ').sum()

# Count the occurrences of each actor
actor_counts = Counter(all_actors)

# Find the most common actor
most_common_actor = actor_counts.most_common(1)[0]

print('\nQ10')
print(most_common_actor)

#QUESTION 11
print("QUESTION 11")
# Split the genres and create a list of all unique genres
unique_genres = set(df['Genre'].str.split(',').explode())

# Count the number of unique genres
num_unique_genres = len(unique_genres)

print('\nQ11')
print(num_unique_genres)

print("QUESTION 12")
# Exclude non-numeric columns
numeric_columns = df.select_dtypes(include='number')

# Calculate the correlation matrix
correlation_matrix = numeric_columns.corr()




