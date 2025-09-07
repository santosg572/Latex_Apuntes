x = 1:12
y = x + round(x + rnorm(12, mean=0, sd=2))

print(x)
print(y)


