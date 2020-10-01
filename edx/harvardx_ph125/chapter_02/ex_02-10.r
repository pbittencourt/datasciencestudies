# Exercises in section 2.10

# import library and open dataset
library(dslabs)
data('murders')

# 1. Use the $ operator to access the population size data and store it as the object pop. Then use the sort function to redefine pop so that it is sorted. Finally, use the [ operator to report the smallest population size.

pop <- murders$population
pop <- sort(pop)
pop[1]

# 2. Now instead of the smallest population size, find the index of the entry with the smallest population size. Hint: use order instead of sort.

pop <- murders$population # reassign to original vector
index <- order(pop)
index[1]
pop[index[1]]

# 3. We can actually perform the same operation as in the previous exercise using the function which.min. Write one line of code that does this.

index_min = which.min(pop)
index_min
index_max = which.max(pop)
index_max

# 4. Now we know how small the smallest state is and we know which row represents it. Which state is it? Define a variable states to be the state names from the murders data frame. Report the name of the state with the smallest population.

states <- murders$state
states[index_min]
states[index_max]

# 5. Use the rank function to determine the population rank of each state from smallest population size to biggest. Save these ranks in an object called ranks, then create a data frame with the state name and its rank. Call the data frame my_df.

ranks <- rank(pop)
my_df = data.frame(state = states, rank = ranks)
my_df

# 6. Repeat the previous exercise, but this time order my_df so that the states are ordered from least populous to most populous. Hint: create an object ind that stores the indexes needed to order the population values. Then use the bracket operator [ to re-order each column in the data frame.

ind = order(pop)
my_df = data.frame(state = states[ind], rank = ranks[ind])
my_df

# 7. The na_example vector represents a series of counts. However, when we compute the average with the function mean, we obtain an NA. The is.na function returns a logical vector that tells us which entries are NA. Assign this logical vector to an object called ind and determine how many NAs does na_example have.

data('na_example')
ind <- is.na(na_example)
length(na_example[ind])

# 8. Now compute the average again, but only for the entries that are not NA. Hint: remember the ! operator.

mean(na_example[!ind])
