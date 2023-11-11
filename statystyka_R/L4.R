# Zadanie 1:

# P(X < 7)
p1 <- punif(7, min = 4, max = 12)
print(p1)

# P(5 < X < 11)
p2 <- punif(11, min = 4, max = 12) - punif(5, min = 4, max = 12)
print(p2)

# P(X > 10)
p3 <- 1 - punif(10, min = 4, max = 12)
print(p3)

# P(X>x)=0.6
x <- qunif(0.4, min = 4, max = 12)
print(x)


# Zadanie 2:
# Ustawienie wektora z wartościami t
t <- seq(0, 3, 0.01)

# Obliczenie gęstości prawdopodobieństwa
lambda <- 4
g <- dexp(t, lambda)

# Narysowanie wykresu gęstości
plot(t, g, type = "l", xlab = "Czas między telefonami", ylab = "Gęstość prawdopodobieństwa")

# Zadanie 3
intensywnosc <- 1/3
# Prawdopodobieństwo, że czas do pierwszej usterki jest większy niż 2 lata
p1 <- pexp(2, rate=intensywnosc, lower.tail=FALSE)
# Prawdopodobieństwo, że czas do pierwszej usterki jest mniejszy niż 4 lata
p2 <- pexp(4, rate=intensywnosc, lower.tail=TRUE)
# Prawdopodobieństwo, że czas do pierwszej usterki jest między 3 a 5 lat
p3 <- pexp(5, rate=intensywnosc, lower.tail=TRUE) - pexp(3, rate=intensywnosc, lower.tail=TRUE)
# Czas t taki, że prawdopodobieństwo iż czas do usterki jest mniejszy niż t wynosi 0,4.
t <- qexp(0.4, rate=intensywnosc, lower.tail=TRUE)

# Wyświetlenie wyników
cat("Prawdopodobieństwo, że czas do pierwszej usterki jest większy niż 2 lata: ", p1, "\n")
cat("Prawdopodobieństwo, że czas do pierwszej usterki jest mniejszy niż 4 lata: ", p2, "\n")
cat("Prawdopodobieństwo, że czas do pierwszej usterki jest między 3 a 5 lat: ", p3, "\n")
cat("Czas t taki, że prawdopodobieństwo iż czas do usterki jest mniejszy niż t wynosi 0,4: ", t, "\n")

# Zadanie 4
mu <- 170
sigma <- 12

p1 <- 1 - pnorm(180, mean = mu, sd = sigma)  # P(X > 180)
p2 <- pnorm(165, mean = mu, sd = sigma)  # P(X < 165)
p3 <- pnorm(190, mean = mu, sd = sigma) - pnorm(155, mean = mu, sd = sigma)  # P(155 < X < 190)

cat("P(X > 180) =", p1, "\n")
cat("P(X < 165) =", p2, "\n")
cat("P(155 < X < 190) =", p3, "\n")

x <- seq(130, 210, length.out = 1000)
y <- dnorm(x, mean = mu, sd = sigma)
plot(x, y, type = "l", xlab = "Wzrost [cm]", ylab = "Gęstość")

