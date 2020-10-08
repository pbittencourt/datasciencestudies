library(dslabs)
data(murders)

# 1. Remake the temperature data frame, adding a line that converts the temperature from Fahrenheit to Celsius.

fahrenheit <- c(35, 88, 42, 84, 81, 30)
celsius <- (5/9) * (fahrenheit - 32)
city <- c("Beijing", "Lagos", "Paris", "Rio de Janeiro",
          "San Juan", "Toronto")
city_temps <- data.frame(name = city, temperature = celsius)
city_temps

# 2. The Basel Problem: the sum of 1 + 1/2² + 1/3² + ... + 1/100² equals to aproximately π²/6

range <- (1:100)
basel <- sum(1/(range^2))
basel

# 3. Compute the per 100,000 murder rate for each state and store it in the object murder_rate. Then compute the average murder rate for the US using the function mean. What is the average?

population <- murders$population
total <- murders$total
murder_rate <- (total / population) * 100000
avg_murder_rate = mean(murder_rate)
avg_murder_rate

# Now we can build a data frame with state and murder rate, from lowest to highest

states <- murders$state
index <- order(murder_rate)
murder_df = data.frame(state = states[index], murder_rate = murder_rate[index])
murder_df

 # We can do the same, but ordering highest to lowest (in this case that's more convenient!)

index <- order(murder_rate, decreasing=TRUE)
murder_df = data.frame(state = states[index], murder_rate = murder_rate[index])
murder_df
