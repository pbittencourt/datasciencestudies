# examples with sort, order and rank

library(dslabs)
data(murders)

total <- murders$total

# sort data, from lowest to highest
sorted <- sort(total)
print('Sorted data:')
sorted

# order data, returning *indexes* corresponding
# with sorted data
indexes <- order(total)
print('Indexes:')
indexes

# return murders$abb INDEXED, ie, in the sequence
# assigned before
murders$abb[indexes]

# return 'ranking' of data, corresponding of
# position the value occupy in the sequence
# from lowest to highest
ranking <- rank(total)
print('Ranking:')
print(ranking)

# max and min functions
max(total)
min(total)

# which max and min?
index_max = which.max(total)
index_min = which.min(total)
index_max
murders$state[index_max]
index_min
murders$state[index_min]
