# Zad 1
# a)
n <- 100
x <- 30
p <- x/n
alpha1 <- 0.05
alpha2 <- 0.01

# Obliczanie przedziałów ufności
z1 <- qnorm(1-alpha1/2)
z2 <- qnorm(1-alpha2/2)
ci1 <- p + c(-1,1)*z1*sqrt(p*(1-p)/n)
ci2 <- p + c(-1,1)*z2*sqrt(p*(1-p)/n)

# Wyświetlenie wyników
cat("Przedział ufności dla 95% poziomu ufności: (", round(ci1[1], 3), ",", round(ci1[2], 3), ")\n")
cat("Przedział ufności dla 99% poziomu ufności: (", round(ci2[1], 3), ",", round(ci2[2], 3), ")\n")

# b)
xbar <- 109
s <- sqrt(225)


# Obliczanie przedziałów ufności
z1 <- qnorm(1-alpha1/2)
z2 <- qnorm(1-alpha2/2)
ci1 <- xbar + c(-1,1)*z1*s/sqrt(n)
ci2 <- xbar + c(-1,1)*z2*s/sqrt(n)

# Wyświetlenie wyników
cat("Przedział ufności dla 95% poziomu ufności: (", round(ci1[1], 3), ",", round(ci1[2], 3), ")\n")
cat("Przedział ufności dla 99% poziomu ufności: (", round(ci2[1], 3), ",", round(ci2[2], 3), ")\n")

# c)

# Obliczanie przedziałów ufności
t1 <- qt(1-alpha1/2, df=n-1)
t2 <- qt(1-alpha2/2, df=n-1)
ci1 <- xbar + c(-1,1)*t1*s/sqrt(n)
ci2 <- xbar + c(-1,1)*t2*s/sqrt(n)

# Wyświetlenie wyników
cat("Przedział ufności dla 95% poziomu ufności: (", round(ci1[1], 3), ",", round(ci1[2], 3), ")\n")
cat("Przedział ufności dla 99% poziomu ufności: (", round(ci2[1], 3), ",", round(ci2[2], 3), ")\n")





# Zad 2
# a)
n <- 100
xbar <- 175
s <- 6

# Poziom ufności
alpha <- 0.1

# Obliczanie przedziału ufności
t <- qt(1 - alpha/2, df = n - 1)
ci <- xbar + c(-1, 1) * t * s / sqrt(n)

# Wyświetlenie wyników
cat("Przedział ufności dla średniego wzrostu (poziom ufności 90%): (", round(ci[1], 3), ",", round(ci[2], 3), ")\n")

# b)
t <- qt(1 - alpha/2, df = n - 1)
ci <- xbar + c(-1, 1) * t * s / sqrt(n)

# c)
# Wartości znane
n <- 100
x <- rnorm(n, mean = 175, sd = 6)
B <- 1000

# Poziom ufności
alpha <- 0.1

# Funkcja do obliczania średniego wzrostu
mean_height <- function(x) {
  return(mean(x))
}

# Obliczanie przedziału ufności
bootstrap_mean <- replicate(B, mean_height(sample(x, replace = TRUE)))
ci <- quantile(bootstrap_mean, c(alpha/2, 1 - alpha/2))

# Wyświetlenie wyników
cat("Przedział ufności dla średniego wzrostu (poziom ufności 90%): (", round(ci[1], 3), ",", round(ci[2], 3), ")\n")





# Zad 3
# a)
# Wartości znane
n <- 50
xbar <- 167
s <- 5

# Poziom ufności
alpha <- 0.02

# Obliczanie przedziału ufności
z <- qnorm(1 - alpha/2)
ci <- xbar + c(-1, 1) * z * s / sqrt(n)

# Wyświetlenie wyników
cat("Przedział ufności dla średniego wzrostu studentek (poziom ufności 98%): (", round(ci[1], 3), ",", round(ci[2], 3), ")\n")

b)
# Wartości znane
n <- 50
xbar <- 167
s <- 5

# Poziom ufności
alpha <- 0.02

# Obliczanie przedziału ufności
t <- qt(1 - alpha/2, df = n - 1)
ci <- xbar + c(-1, 1) * t * s / sqrt(n)

# Wyświetlenie wyników
cat("Przedział ufności dla średniego wzrostu studentek (poziom ufności 98%): (", round(ci[1], 3), ",", round(ci[2], 3), ")\n")

# c)
# Wartości znane
n <- 50
x <- rnorm(n, mean = 167, sd = 5)
B <- 1000

# Poziom ufności
alpha <- 0.02

# Funkcja do obliczania średniego wzrostu
mean_height <- function(x) {
  return(mean(x))
}

# Obliczanie przedziału ufności
bootstrap_mean <- replicate(B, mean_height(sample(x, replace = TRUE)))
ci <- quantile(bootstrap_mean, c(alpha/2, 1 - alpha/2))

# Wyświetlenie wyników
cat("Przedział ufności dla średniego wzrostu studentek (poziom ufności 98%): (", round(ci[1], 3), ",", round(ci[2], 3), ")\n")






# Zad 4
# a)
# Wartości znane
n <- 100
x <- 30
p <- x/n

# Poziom ufności
alpha <- 0.06

# Obliczanie przedziału ufności
z <- qnorm(1 - alpha/2)
se <- sqrt(p*(1-p)/n)
ci <- p + c(-1, 1) * z * se

# Wyświetlenie wyników
cat("Przedział ufności dla proporcji studentów o wzroście przekraczającym 168cm (poziom ufności 94%): (", round(ci[1], 3), ",", round(ci[2], 3), ")\n")

# b)
# Wartości znane
n <- 100
x <- 30
B <- 1000

# Poziom ufności
alpha <- 0.06

# Funkcja do obliczania proporcji
prop_height <- function(x, n) {
  return(sum(x > 168) / n)
}

# Obliczanie przedziału ufności
bootstrap_prop <- replicate(B, prop_height(sample(x, replace = TRUE), n))
ci <- quantile(bootstrap_prop, c(alpha/2, 1 - alpha/2))

# Wyświetlenie wyników
cat("Przedział ufności dla proporcji studentów o wzroście przekraczającym 168cm (poziom ufności 94%): (", round(ci[1], 3), ",", round(ci[2], 3), ")\n")





# Zad 5
# a)

# Wartości znane
n <- 60
x <- 15
p <- x/n

# Poziom ufności
alpha <- 0.04

# Obliczanie przedziału ufności
z <- qnorm(1 - alpha/2)
se <- sqrt(p*(1-p)/n)
ci <- p + c(-1, 1) * z * se

# Wyświetlenie wyników
cat("Przedział ufności dla proporcji studentek o wzroście przekraczającym 168cm (poziom ufności 96%): (", round(ci[1], 3), ",", round(ci[2], 3), ")\n")

# b)
# Wartości znane
n <- 60
x <- 15
B <- 1000

# Poziom ufności
alpha <- 0.04

# Funkcja do obliczania proporcji
prop_height <- function(x, n) {
  return(sum(x > 168) / n)
}

# Obliczanie przedziału ufności
bootstrap_prop <- replicate(B, prop_height(sample(x, replace = TRUE), n))
ci <- quantile(bootstrap_prop, c(alpha/2, 1 - alpha/2))

# Wyświetlenie wyników
cat("Przedział ufności dla proporcji studentek o wzroście przekraczającym 168cm (poziom ufności 96%): (", round(ci[1], 3), ",", round(ci[2], 3), ")\n")
