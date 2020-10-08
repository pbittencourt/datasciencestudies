x <- c(2, 43, 27, 96, 18)
sort(x)
order(x)
rank(x)
min(x)
which.min(x)
which.max(x)

# Mandi, Amy, Nicole, and Olivia all ran different distances in different time intervals. Their distances (in miles) and times (in minutes) are as follows:

name <- c("Mandi", "Amy", "Nicole", "Olivia")
distance <- c(0.8, 3.1, 2.8, 4.0)
time <- c(10, 30, 40, 50)
timeHour <- time / 60
timeHour
speed <- distance / timeHour
speed
