##########################
# SECTION 2.13: INDEXING #
##########################

# open dataset
library(dslabs)
data('murders')

# define population, total and state
population <- murders$population
total <- murders$total
state <- murders$state

# ------------------------
# Subsetting with logicals
# ------------------------

# calculating murders rate per population
rate <- total / population * 100000

# which state have murder rates inferior than 0.71?
index <- rate < 0.71
index
state[index]

# logical operators are integers, also. we can sum up them!
# hence, how many state have murder rates inferior than 0.71?
sum(index)

# ------------------------
# Logical operators
# ------------------------

# the logical operator AND (&) return return TRUE when both
# of the given conditions are true.

# select state with murder rates equal or inferior than 1.2
# and located on the west:
safe <- rate <= 1.0
west <- murders$region == 'West'
index <- safe & west
state[index]

# ------------------------
# Which, match and %in%
# ------------------------

# The function `which` tells us which entries of a logical vector are TRUE.
# We can acess the murder rate of California:
ind <- which(state == "California")
rate[ind]

# The `match` function tells us which indexes of a second vector match each of the entries of a first vector.
# Say we wish to subsect the states vector, containing only New York, Florida and Texas:
ind <- match(c("New York", "Florida", "Texas"), state)
ind

# Thus, we can look at the rates of these states:
rate[ind]

# The `%in%` operator is kinda like the same in python: it tells us whether or not each element of a first vector is in a second.
# Let’s imagine you are not sure if Boston, Dakota, and Washington are states. You can find out like this:
c("Boston", "Dakota", "Washington") %in% state
