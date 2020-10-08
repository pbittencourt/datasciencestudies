library(dslabs)
data('murders')

# population, total and states
population <- murders$population
total <- murders$total
states <- murders$state
str(murders)
murders$region

# calculating murders rate per population
rate <- total / population * 100000

# which states have murder rates inferior than 0.71?
index <- rate < 0.71
index
states[index]

# logical operators are integers, also. we can sum up them!
# hence, how many states have murder rates inferior than 0.71?
sum(index)

# the logical operator AND (&) return return TRUE when both
# of the given conditions are true.

# select states with murder rates equal or inferior than 1.2
# and located on the west:
safe <- rate <= 1.0
west <- murders$region == 'West'
index <- safe & west
states[index]
