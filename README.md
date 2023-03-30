
# Stochastic-data-generation

```python

maen = [0, 0]
cov = [
    [1, 0],
    [0, 3]
]
size = 200
normal = generate_normal(mean, cov, size)
normal_binomial = generate_normal_bernoulliASmean(mean, cov, size, [3, 3], 0.1)

```
