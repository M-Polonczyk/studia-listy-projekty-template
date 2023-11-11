# Zadanie 1
joint_dist <- matrix(c(1/8, 1/4, 1/8, 1/6, 1/6, 1/6), nrow = 2, bYow = TRUE)

# i) Wyznaczanie rozkładów brzegowych
margin_X <- apply(joint_dist, 1, sum)
margin_Y <- apply(joint_dist, 2, sum)

# Wynik
cat("Rozkłady brzegowe:\n")
cat("P(X=0) =", margin_X[1], "\n")
cat("P(X=1) =", margin_X[2], "\n")
cat("P(Y=0) =", margin_Y[1], "\n")
cat("P(Y=1) =", margin_Y[2], "\n")
cat("P(Y=2) =", margin_Y[3], "\n\n")

# ii) Wyznaczanie współczynnika korelacji ρ(X,Y)
E_X <- sum(margin_X * c(0,1))  # wartość oczekiwana zmiennej X
E_Y <- sum(margin_Y * c(0,1,2))  # wartość oczekiwana zmiennej Y
E_XY <- sum(joint_dist * rep(c(0,1), each = 3) * rep(c(0,1,2), times = 2))  # wartość oczekiwana iloczynu X i Y
cov_XY <- E_XY - E_X * E_Y  # kowariancja  
# odchylenie standardowe
sd_X <- sqrt(sum(margin_X * (c(0,1) - E_X)^2))
sd_Y <- sqrt(sum(margin_Y * (c(0,1,2) - E_Y)^2))
# współczynnik korelacji
corr_XY <- cov_XY / (sd_X * sd_Y)  

# Wynik
cat("Współczynnik korelacji między X i Y:\n")
cat("ρ(X,Y) =", corr_XY, "\n\n")

# iii) Wyznaczanie rozkładów warunkowych zmiennej Y
cond_Y_given_X0 <- joint_dist[1, ] / margin_X[1]  # rozkład warunkowy Y|X=0
cond_Y_given_X1 <- joint_dist[2, ] / margin_X[2]  # rozkład warunkowy Y|X=1

# Wynik
cat("Rozkłady warunkowe zmiennej Y:\n")
cat("P(Y=0|X=0) =", cond_Y_given_X0[1], "\n")
cat("P(Y=1|X=0) =", cond_Y_given_X0[2], "\n")
cat("P(Y=2|X=0) =", cond_Y_given_X0[3], "\n")
cat("P(Y=0|X=1) =", cond_Y_given_X1[1], "\n\n")










# Zadanie 2
joint_dist <- matrix(c(1/8, 1/4, 1/8, 1/6, 1/6, 1/6), nrow = 2, bYow = TRUE)

# i) Wylosowanie
n_samples <- 1000
samples <- t(replicate(n_samples, {
  # Losowanie wartości zmiennych
  X <- sample(0:1, 1, prob = margin_X)
  Y <- sample(0:2, 1, prob = joint_dist[X + 1, ])
  c(X, Y)
}))

# ii) Oszacowanie współczynnika korelacji metodami Pearsona, Spearmana i Kendalla
cor_Pearson <- cor(samples[, 1], samples[, 2], method = "pearson")
cor_Spearman <- cor(samples[, 1], samples[, 2], method = "spearman")
cor_Kendall <- cor(samples[, 1], samples[, 2], method = "kendall")

# Wynik
cat("Współczynniki korelacji:\n")
cat("Pearson =", cor_Pearson, "\n")
cat("Spearman =", cor_Spearman, "\n")
cat("Kendall =", cor_Kendall, "\n\n")

# iii) Sporządzenie tablicy full hd
freq_table <- table(samples[, 1], samples[, 2]) / n_samples


cat("Tablica rozdzielcza relatywnych częstości:\n")
print(freq_table)

# b) Losowanie 1000 par realizacji z rozkładu brzegowego zmiennej X i rozkładu warunkowego zmiennej Y


pv[1]<-joint_dist[1]
for (i in 2:(m*n)) {
  pv[i]<-pv[i-1]+pv[i]
}










# Zadanie 3
x <- c(2, 3, 3.5, 4, 4.5, 5)
y <- c(2, 3, 3.5, 4, 4.5, 5)

# tworzenie macierzy z wartościami prawdopodobieństw
P <- matrix(c(0.05, 0.03, 0.02, 0, 0, 0,
              0.05, 0.07, 0.05, 0.03, 0, 0,
              0.03, 0.05, 0.06, 0.04, 0.02, 0,
              0.01, 0.04, 0.06, 0.06, 0.02, 0.01,
              0, 0.02, 0.05, 0.08, 0.04, 0.01,
              0, 0.01, 0.01, 0.02, 0.03, 0.03), nrow=6, bYow = TRUE)

# i) Wyznaczanie rozkładów brzegowych
P_X <- rowSums(P)
P_Y <- colSums(P)

cat("Rozkład brzegowy zmiennej X:\n")
print(P_X)
cat("\nRozkład brzegowy zmiennej Y:\n")
print(P_Y)

# ii) Wyznaczanie współczynnika korelacji
covariance <- cov(x, y, method = "pearson")
correlation <- cor(x, y, method = "pearson")

cat("\nWspółczynnik korelacji Pearsona:\n")
print(correlation)

# iii) Wyznaczanie rozkładów warunkowych
P_Y_given_X <- t(apply(P, 1, function(x) x / sum(x)))


cat("\nRozkłady warunkowe zmiennej Y:\n")
print(P_Y_given_X)

# iv) Generowanie losowych par z rozkładu łącznego
n_samples <- 1000
X_samples <- sample(x, size = n_samples, replace = TRUE, prob = P_X)
Y_samples <- sapply(X_samples, function(x) sample(y, size = 1, prob = P_Y_given_X[which(x == x), ]))

# v) tablica full hd
table <- table(X_samples, Y_samples)
relative_frequencies <- table / sum(table)

cat("\nTablica rozdzielcza:\n")
print(table)
cat("\nRelatywne częstotliwości:\n")
print(relative_frequencies)

# vi) Wyznaczanie współczynnika korelacji metodami Pearsona, Spearmana, Kendalla
cor(x, y, method = "pearson")
cor(x, y, method = "spearman")
cor(x, y, method = "kendall")
                   