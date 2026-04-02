# Log-normal Distribution

## Definition
A positive random variable $X$ is log-normally distributed with parameters $\mu$ and $\sigma>0$ if
$$\ln X\sim\mathcal{N}(\mu,\sigma^2).$$
Equivalently, if $Y\sim\mathcal{N}(\mu,\sigma^2)$ then $X=\exp(Y)$ has a log-normal distribution.

## Probability Density Function (PDF)
For $x>0$,
$$f(x;\mu,\sigma)=\frac{1}{x\sigma\sqrt{2\pi}}\exp\left(-\frac{(\ln x-\mu)^2}{2\sigma^2}\right).$$

## Cumulative Distribution Function (CDF)
$$F(x;\mu,\sigma)=\Phi\left(\frac{\ln x-\mu}{\sigma}\right),\qquad x>0$$
where $\Phi$ is the standard normal CDF.

## Moments and Summary Statistics
- Mean: $\displaystyle E[X]=e^{\mu+\tfrac{1}{2}\sigma^2}$.  
- Median: $\displaystyle \mathrm{median}(X)=e^{\mu}$.  
- Mode: $\displaystyle \mathrm{mode}(X)=e^{\mu-\sigma^2}$.  
- Variance: $\displaystyle \mathrm{Var}(X)=(e^{\sigma^2}-1)e^{2\mu+\sigma^2}$.  
- General moments: $\displaystyle E[X^n]=e^{n\mu+\tfrac{1}{2}n^2\sigma^2}.$

Note: the moment-generating function $M_X(t)=E[e^{tX}]$ does not exist for $t>0$ (it diverges) when $\sigma>0$.

## Parameter Interpretation
The parameters $\mu$ and $\sigma$ are the mean and standard deviation of the log of the variable (the underlying normal distribution). They control the location and multiplicative spread of $X$.

## When to use
Use the log-normal model for positive-valued, right-skewed data that appear multiplicative in nature (e.g., incomes, biological sizes, time-to-failure for some processes, and certain financial returns when modeling prices instead of log-returns).

## Estimation
A simple estimator is to transform data $x_i$ via $y_i=\ln x_i$ and fit a normal distribution to $y_i$ (use sample mean and sample standard deviation as MLEs for $\mu$ and $\sigma$).

## Sampling with NumPy (example)
```python
import numpy as np
mu = 0.0       # mean of ln(X)
sigma = 1.0    # std dev of ln(X)
samples = np.random.lognormal(mean=mu, sigma=sigma, size=1000)
```

## Notes & References
- Log-normal arises naturally when a quantity is the product of many independent positive factors (central limit theorem on the log scale).
- See standard texts or the Wikipedia entry "Log-normal distribution" for more details and proofs.
