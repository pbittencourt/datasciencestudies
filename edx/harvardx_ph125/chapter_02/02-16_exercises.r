library(dslabs)
data('murders')

# 1. We made a plot of total murders versus population and noted a strong relationship. Not surprisingly, states with larger populations had more murders. Transform the variables using the log10 transformation and then plot them.

pop_in_millions <- murders$population / 10^6
total <- murders$total
plot(log10(pop_in_millions), log10(total))

# 2. Create a histogram of the state populations.

x <- with(murders, total / population * 10^6)
hist(x)

# 3. Generate boxplots of the state populations by region.

murders$rate <- with(murders, total / population * 100000)
boxplot(rate~region, data = murders)
