library(dslabs)
data(murders)

# basic plot function

x <- murders$population
y <- murders$total * 10^6
plot(x, y)

# for a quick plot that avoids accessing variables twice,
# we can use the `with` function.
# it lets us use the `murders` column names in the `plot` function.
# it also works with any data frames and any function.

with(murders, plot(population, total))

# it's simple to make a histogram using `hist` function:

x <- with(murders, total / population * 10^6)
hist(x)

# boxplots can be used to compare data:

murders$rate <- with(murders, total / population * 10^6)
boxplot(rate~region, data = murders)

# the image function displays the values in a matrix using color:

x <- matrix(1:120, 12, 10)
image(x)
