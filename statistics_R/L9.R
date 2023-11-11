# Zad 1
# Obliczenie liczby obserwacji
n <- 100

# Obliczenie średniego IQ
mean_iq <- 109

# Obliczenie wariancji IQ
var_iq <- 225

# Wartość hipotetyczna
mu_0 <- 105

# Poziom istotności
alpha <- 0.05

# Obliczenie wartości testu Z
z <- (mean_iq - mu_0) / sqrt(var_iq/n)

# Obliczenie wartości p dla testu Z
p_value_z <- 2 * (1 - pnorm(abs(z)))

# Obliczenie wartości krytycznej dla testu Z
z_critical <- qnorm(1 - alpha/2)




# Zad 2

# Wczytanie danych z pliku "waga1.csv"
data <- read.csv("waga1.csv")

n <- length(data$Wzrost)

# Obliczenie średniego wzrostu
mean_height <- mean(data$Wzrost)

# Wartość hipotetyczna
mu_0 <- 168

# Poziom istotności
alpha <- 0.05

# Obliczenie wartości testu Z
z <- (mean_height - mu_0) / (sd(data$Wzrost) / sqrt(n))

# Obliczenie wartości p dla testu Z
p_value_z <- 2 * (1 - pnorm(abs(z)))

# Obliczenie wartości krytycznej dla testu Z
z_critical <- qnorm(1 - alpha/2)



# Wykonanie testu t (test Studenta)
t_test <- t.test(data$Wzrost, mu = mu_0)



# Wykonanie testu t za pomocą funkcji t.test
t_test_function <- t.test(data$Wzrost, mu = mu_0)

# Wykonanie testu t (test Studenta)
t_test <- t.test(data$IQ, mu = mu_0)




# Zad 3


male_data <- subset(data, plec == 1)

# Obliczenie liczby obserwacji dla studentów męskich
n <- length(male_data$Wzrost)

# Obliczenie średniego wzrostu dla studentów męskich
mean_height <- mean(male_data$Wzrost)

# Wartość hipotetyczna
mu_0 <- 172

# Poziom istotności
alpha <- 0.05

# Obliczenie wartości testu Z
z <- (mean_height - mu_0) / (sd(male_data$Wzrost) / sqrt(n))

# Obliczenie wartości p dla testu Z
p_value_z <- 2 * (1 - pnorm(abs(z)))

# Obliczenie wartości krytycznej dla testu Z
z_critical <- qnorm(1 - alpha/2)



# Wykonanie testu t (test Studenta)
t_test <- t.test(male_data$Wzrost, mu = mu_0)



# Wykonanie testu t za pomocą funkcji t.test
t_test_function <- t.test(male_data$Wzrost, mu = mu_0)



# Zad 4


n <- length(data$Waga)

# Obliczenie średniej masy ciała
mean_weight <- mean(data$Waga)

# Wartość hipotetyczna
mu_0 <- mean_weight - 2

# Poziom istotności
alpha <- 0.05

# Obliczenie wartości testu Z
z <- (mean_weight - mu_0) / (sd(data$Waga) / sqrt(n))

# Obliczenie wartości p dla testu Z
p_value_z <- 2 * (1 - pnorm(abs(z)))

# Obliczenie wartości krytycznej dla testu Z
z_critical <- qnorm(1 - alpha/2)

t_test <- t.test(data$Waga, mu = mu_0)
# t.test
t_test_function <- t.test(data$Waga, mu = mu_0)




# Zad 5

# Wyodrębnienie danych dotyczących studentów męskich
male_data <- subset(data, plec == 1)

# Obliczenie liczby obserwacji dla studentów męskich
n <- length(male_data$Waga)

# Obliczenie średniej masy ciała dla studentów męskich
mean_weight <- mean(male_data$Waga)

# Wartość hipotetyczna
mu_0 <- mean_weight - 4

# Poziom istotności
alpha <- 0.05

# Obliczenie wartości testu Z
z <- (mean_weight - mu_0) / (sd(male_data$Waga) / sqrt(n))

# Obliczenie wartości p dla testu Z
p_value_z <- 2 * (1 - pnorm(abs(z)))

# Obliczenie wartości krytycznej dla testu Z
z_critical <- qnorm(1 - alpha/2)


# test
t_test <- t.test(male_data$Waga, mu = mu_0)

cat("Wartość testu t:", t_test$statistic, "\n")
cat("Wartość p:", t_test$p.value, "\n")
cat("Wartość krytyczna (dla alpha/2):", t_test$conf.int[1], "\n")
cat("Wartość krytyczna (dla 1-alpha/2):", t_test$conf.int[2], "\n")


# t.test
t_test_function <- t.test(male_data$Waga, mu = mu_0)


