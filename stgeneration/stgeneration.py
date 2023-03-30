import numpy as np
from scipy import stats

# define mean and covariance matrix of bivariate normal distribution
# mean = [0, 0]
# cov = [[1, 0.5], [0.5, 1]]

# generate 1000 samples from the bivariate normal distribution
def generate_normal(
    mean: list[float],
    cov: list[list[float]],
    size: int
):
    return np.random.multivariate_normal(mean, cov, size=size)


def generate_normal_bernoulliASmean(
    mean: list[float],
    cov: list[list[float]],
    size: int,
    binomial_maen: list[float],
    p_success: float
):

    bernoulli_sample = stats.bernoulli.rvs(p=p_success, size=size)[:, np.newaxis]
    binomial_maen_tile = np.tile(binomial_maen, (size,1))
    ret = generate_normal(mean, cov, size) + bernoulli_sample * binomial_maen_tile
    return  ret


if __name__ == '__main__':
    mean = [0, 0]
    cov = [
        [1, 0],
        [0, 3]
    ]
    size = 200
    normal = generate_normal(mean, cov, size)
    normal_binomial = generate_normal_bernoulliASmean(mean, cov, size, [3, 3], 0.1)

    print('normal:', normal.shape)
    print('normal_binomial:', normal_binomial.shape)
