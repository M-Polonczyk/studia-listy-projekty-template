# instalacja ggplot2, jeśli nie jest jeszcze zainstalowana
install.packages("ggplot2")
library(ggplot2)

# Zad 1

x1 <- pnorm(160, mean = 170, sd = 12)
x2 <- 1 - pnorm(180, mean = 170, sd = 12)
x1_2 <- pnorm(180, mean = 170, sd = 12) - pnorm(160, mean = 170, sd = 12)
k = qnorm(0.15, mean = 170, sd = 12, lower.tail = FALSE)


# Zad 2

#i)
n <- 10000

U1 <- runif(n)
U2 <- runif(n)
Z <- cos(2*pi*U1)*sqrt(-2*log(U2))

#ii)
par(mfrow = c(1, 2))
x <- seq(-4, 4, by = 0.01)
ggplot(data.frame(x=c(0, 400)), aes(x)) +
  geom_line(aes(y=dnorm((x-100)/15)/15), color="blue")   # gęstość rozkładu normalnego o średniej 100 i wariancji 15
  


#iii)
# funkcja do obliczania estymatora jądrowego gęstości
kernel_density <- function(x, h) {
  n <- length(x)
  dens <- rep(0, n)
  for (i in 1:n) {
    dens[i] <- mean(dnorm((x[i]-x)/h)/h)
  }
  dens
}
Y <- 100 + 15*Z

# wyznaczenie estymatora jądrowego gęstości
h <- 3
dens_Y <- data.frame(x=Y, y=kernel_density(Y, h))



# Zad 3

X <- rnorm(n = 2000, mean = 170, sd = 12)
Z <- (X - 170) / 12
#plot(density(Z), col = "lightblue", lwd = 2, main = "Estymator jądrowy gęstości dla Z = (X - 170) / 12")
x <- seq(-4, 4, length.out = 100)
y <- dnorm(x)
#lines(x, y, col = "red", lwd = 2)
#legend("topright", legend = c("Estymator jądrowy gęstości", "Rozkład normalny standardowy"), 
#       col = c("lightblue", "red"), lty = 1, lwd = 2)


# Zad 4

# i)
# generowanie 1000 realizacji zmiennej S1
S1 <- rexp(n=1000, rate=0.5)
Z1 <- (S1 - mean(S1)) / sd(S1) 

# generowanie 1000 realizacji zmiennej S20
S20 <- sum(rexp(n=20*1000, rate=0.5), by=20)
Z20 <- (S20 - mean(S20)) / sd(S20) 

# generowanie 1000 realizacji zmiennej S200
S200 <- sum(rexp(n=200*1000, rate=0.5), by=200)
Z200 <- (S200 - mean(S200)) / sd(S200)

# ii)
# porównanie
kde <- function(x) density(x, kernel="gaussian", bw="nrd0")

S1 <- rexp(n=1000, rate=0.5)
Z1 <- (S1 - mean(S1)) / sd(S1)
S20 <- sum(rexp(n=20*1000, rate=0.5), by=20)
Z20 <- (S20 - mean(S20)) / sd(S20)
S200 <- sum(rexp(n=200*1000, rate=0.5), by=200)
Z200 <- (S200 - mean(S200)) / sd(S200)

# sporządzenie wykresów
ggplot() +
  geom_density(data=data.frame(Z=Z1), aes(x=Z, y=..density..), color="blue") +
  stat_function(fun=dnorm, args=list(mean=0, sd=1), color="red", size=1)
                
# iii)
samples_1 <- rbinom(1000, 30, 0.5)
samples_2 <- rbinom(1000, 100, 0.5)
samples_3 <- rbinom(1000, 30, 0.1)
samples_4 <- rbinom(1000, 100, 0.1)

# wyznaczenie średniej i odchylenia standardowego
mean_1 <- mean(samples_1)
sd_1 <- sd(samples_1)
mean_2 <- mean(samples_2)
sd_2 <- sd(samples_2)
mean_3 <- mean(samples_3)
sd_3 <- sd(samples_3)
mean_4 <- mean(samples_4)
sd_4 <- sd(samples_4)

# wyznaczenie teoretycznej gęstości
x <- 0:30
density_1 <- dnorm(x, mean_1, sqrt(mean_1*(1-mean_1)))
density_2 <- dnorm(x, mean_2, sqrt(mean_2*(1-mean_2)))
density_3 <- dnorm(x, mean_3, sqrt(mean_3*(1-mean_3)))
density_4 <- dnorm(x, mean_4, sqrt(mean_4*(1-mean_4)))

# wyznaczenie relatywnych częstości
freq_1 <- table(samples_1) / length(samples_1)
freq_2 <- table(samples_2) / length(samples_2)
freq_3 <- table(samples_3) / length(samples_3)
freq_4 <- table(samples_4) / length(samples_4)

# wykres porównujący relatywne częstości z gęstością normalną
plot(x, density_1, type="l", ylim=c(0,0.2), ylab="Gęstość", xlab="x")
points(x, freq_1, pch=20, col="blue")
legend("topright", legend=c("Gęstość normalna", "Relatywne częstości"), pch=c(NA, 20), col=c("black", "blue"))

plot(x, density_2, type="l", ylim=c(0,0.2), ylab="Gęstość", xlab="x")
points(x, freq_2, pch=20, col="blue")
legend("topright", legend=c("Gęstość normalna", "Relatywne częstości"), pch=c(NA, 20), col=c("abc"))
