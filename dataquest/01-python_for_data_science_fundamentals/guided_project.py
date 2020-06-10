# DATAQUEST.IO GUIDED PROJECT
"""
Profitable App Profiles for the App Store and Google Play Markets
Created by Pedro P. Bittencourt
v0.1
"""

from csv import reader  # module to handle csv files
from operator import itemgetter  # module to sort dictionary by values
from utilities.interface import *
from utilities.data import *
from utilities.logical import *

###############################
#  OPENING AND CLEANING DATA  #
###############################

# open android and ios datasets
android_header, android = open_dataset('googleplaystore.csv')
ios_header, ios = open_dataset('AppleStore.csv')

# delete android's line 10472 _ contains 12 columns instead of 13
del android[10472]

reviews_max = {}
for app in android:
    name = app[0]
    n_reviews = float(app[3])

    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
    if name not in reviews_max:
        reviews_max[name] = n_reviews

android_clean = []
already_added = []
for app in android:
    name = app[0]
    n_reviews = float(app[3])

    if n_reviews == reviews_max[name] and name not in already_added:
        android_clean.append(app)
        already_added.append(name)

android_english = []
for app in android_clean:
    name = app[0]
    if is_english(name):
        android_english.append(app)

ios_english = []
for app in ios:
    name = app[1]
    if is_english(name):
        ios_english.append(app)

android_final = []
for app in android_english:
    price = app[7]
    if price == '0':
        android_final.append(app)

ios_final = []
for app in ios_english:
    price = app[5]
    if price == '0':
        ios_final.append(app)

###############################
#  EXPLORING DATA             #
###############################

# # extracts genres from ios dataset and generates a freq. table from it
# genres_ios = freq_table(extract(ios_final, -5))
#
# # initialize an empty list that will contain all avg ratings
# genres_list = list()
#
# # main loop: loop through each genre in genres list
# for genre in genres_ios:
#
#     # initialize the total number of ratings
#     total = 0
#     # initialize the total number of apps
#     len_genre = 0
#
#     # second loop: now, loop through all apps in ios dataset
#     for app in ios_final:
#
#         # fetch the genre of this app
#         genre_app = app[-5]
#
#         # check if this genre is the same as the genre of the main loop
#         if genre_app == genre:
#
#             # fetch the no. of ratings of this app
#             n_ratings = float(app[6])
#
#             # increase total of ratings and number of apps
#             total += n_ratings
#             len_genre += 1
#
#     # calculates the average rating
#     avg_ratings = total / len_genre
#
#     # prints the genre and its average rating
#     # print(genre, ':', avg_ratings)
#
#     # append tuple(ratings, genre) to genres_list
#     # this awkward order will be used to simplify sorting
#     a_tuple = (avg_ratings, genre)
#     genres_list.append(a_tuple)
#
# # end of main loop
#
# for key in sorted(genres_list, reverse=True):
#     print('{}: {:.2f}'.format(key[1], key[0]))

# extracts categories from android dataset and generates a freq. table from it
categories_android = freq_table(extract(android_final, 1))

# initialize an empty list that will contain all avg installs by category
categories_list = list()

# main loop: loop through each category in categories list
for category in categories_android:

    # initialize the total number of installs
    total = 0
    # initialize the total number of apps
    len_category = 0

    # second loop: now, loop through all apps in android dataset
    for app in android_final:

        # fetch the category of this app
        category_app = app[1]

        # check if this category is the same as the category of the main loop
        if category_app == category:

            # fetch the no. of installs of this app
            n_installs = app[5]

            # removes ',' and '+' symbols from installs number
            n_installs = n_installs.replace(',', '')
            n_installs = n_installs.replace('+', '')

            # increase total of installs and number of apps
            total += float(n_installs)
            len_category += 1

    # calculates the average number of installs
    avg_n_installs = total / len_category

    # # prints the genre and its average rating
    # print(category, ':', avg_n_installs)

    # append tuple(installs, category) to categories_list
    # this awkward order will be used to simplify sorting
    tuple_installs_category = (avg_n_installs, category.replace('_', ' '))
    categories_list.append(tuple_installs_category)

# end of main loop

for key in sorted(categories_list, reverse=True):
    print('{}: {:.2f}'.format(key[1], key[0]))

line()

print('Communication apps in 1,000,000,000+ installs range:')
for app in android_final:
    if app[1] == 'COMMUNICATION' and app[5] == '1,000,000,000+':
        print(app[0], ':', app[5])

line()

print('Communication apps in 500,000,000+ installs range:')
for app in android_final:
    if app[1] == 'COMMUNICATION' and app[5] == '500,000,000+':
        print(app[0], ':', app[5])
