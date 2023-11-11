# Zadanie 1
set.seed(123) 
x1 <- runif(5000, 0, 1) 
x2 <- rnorm(3000, 100, 15)


hist(x1, breaks = 30, main = "Histogram - rozkład jednostajny")
hist(x2, breaks = 30, main = "Histogram - rozkład normalny")

# ii) 
d1 <- density(x1)
plot(d1, main = "Estymator jądrowy - rozkład jednostajny")
d2 <- density(x2)
plot(d2, main = "Estymator jądrowy - rozkład normalny")

# Zadanie 2

# Symulacja 600 rzutów kostką
x3 <- sample(1:6, 600, replace = TRUE)
mean_x3 <- mean(x3) # średnia z próby
var_x3 <- var(x3) # wariancja z próby
freq_x3 <- table(x3) # rozkład częstości
freq_x3
# porównanie z rozkładem jednostajnym
freq_unif <- table(sample(1:6, 600, replace = TRUE))
freq_unif
# wniosek: więcej skrajnych wartości w przypadku 1
# > freq_x3
# x3
# 1   2   3   4   5   6 
# 105  98  95  91 102 109 
# > freq_unif
# 1   2   3   4   5   6 
# 90  88 119  87 104 112 

# ii)
data_frame = as.data.frame(freq_x3)
var(data_frame)

# iii) 
x4 <- sample(1:6, 600, replace = TRUE)
mean_x4 <- mean(x4)
var_x4 <- var(x4)
freq_x4 <- table(x4)
freq_x4

# Zadanie 3
x5 <- sample(0:3, 600, replace = TRUE, prob = c(0.3, 0.4, 0.2, 0.1)) 
mean_x5 <- mean(x5) # średnia z próby
sd_x5 <- sd(x5) # odchylenie standardowe z próby
freq_x5 <- table(x5) # rozkład częstości
freq_x5

# Zadanie 4
set.seed(123)
x6 <- rbinom(100, 10, 0.3)
x7 <- rgeom(50, 0.4)

# Zadanie 5
lambda <- 3
n <- 50
poisson_samples <- vector(mode = "integer", length = n)

i <- 1
while (i <= n) {
  x <- 0
  p <- exp(-lambda)
  F <- p
  u <- runif(1)
  while (u > F) {
    x <- x + 1
    p <- p * lambda / x
    F <- F + p
  }
  poisson_samples[i] <- x
  i <- i + 1
}

poisson_samples

# Zadanie 6
# funkcja odwrotności dystrybuanty
Finv <- function(u) {
  ifelse(u <= 0.5, sqrt(2*u), 2 - sqrt(2 - 2*u))
}

set.seed(123) # ziarno losowości
u <- runif(200) # 200 wartości z rozkładu równomiernego na przedziale [0,1]
x <- Finv(u) 

hist(x, breaks = 20, main = "Histogram 200 realizacji z rozkładu g(x) \n (metoda odwracania dystrybuanty)", xlab = "x")

g <- function(x) {
  ifelse(x >= 0 & x <= 2, 0.5*x, 0)
}  
