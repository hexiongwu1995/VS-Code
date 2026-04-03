#set page(paper: "a4", margin: (x: 1.8cm, y: 1.6cm))
#set text(font: "Times New Roman", size: 10.5pt)
#set par(justify: true, leading: 0.7em)

= How the Normal Distribution Arises

The normal distribution appears whenever many small, nearly independent effects are added and then standardized. The central limit theorem explains the limit, while symmetry and finite variance explain why the limiting shape must be Gaussian.

== 1. Standardizing a Sum

Let

$
S_n = X_1 + X_2 + dots + X_n.
$

Assume each $X_i$ has mean $mu$ and variance $sigma^2$.

Define the normalized sum

$
Z_n = (S_n - n mu) / (sigma sqrt(n)).
$

Its characteristic function is

$
phi_(Z_n)(t) = exp(- i t mu sqrt(n) / sigma) (phi_X(t / (sigma sqrt(n))))^n.
$

For small $u$, a second-order expansion gives

$
phi_X(u) = 1 + i mu u - 1 / 2 sigma^2 u^2 + epsilon(u)
$

after centering. Therefore

$
log phi_(Z_n)(t) = - t^2 / 2 + epsilon_n(t),
quad
phi_(Z_n)(t) -> exp(- t^2 / 2).
$

So the standardized sum converges in distribution to the standard normal law:

$Z_n$ tends to the standard normal distribution $N(0, 1)$.

== 2. Why the Limit Has the Gaussian Form

Suppose a centered density keeps the same shape after convolution and rescaling. If $F(t)$ is its Fourier transform, stability under adding two independent copies implies

$
F(t)^2 = F(sqrt(2) t).
$

Write $g(t) = log F(t)$. Then

$
2 g(t) = g(sqrt(2) t).
$

With continuity, symmetry, and finite variance, the only solutions are quadratic:

$
g(t) = - c t^2,
quad
c > 0.
$

Hence

$
F(t) = exp(- c t^2),
$

and the inverse Fourier transform gives

$
f(x) = 1 / sqrt(2 pi sigma^2) exp(- x^2 / (2 sigma^2)).
$

This is exactly the Gaussian density.

== 3. A Variational View

Among all densities with fixed mean and variance, the normal density is the one with maximum entropy

$
H(f) = - integral f(x) log f(x) dif x.
$

Imposing the constraints

$
integral f(x) dif x = 1,
quad
integral x f(x) dif x = mu,
quad
integral (x - mu)^2 f(x) dif x = sigma^2,
$

the Euler-Lagrange equation yields

$
log f(x) = a + b x + c x^2,
quad
c < 0.
$

So the optimizer must have the form

$
f(x) = A exp(- (x - mu)^2 / (2 sigma^2)),
$

again the normal distribution.

== Plots

#figure(
  table(
    columns: 2,
    inset: 6pt,
    stroke: none,
    image("normal_density.svg", width: 100%),
    image("clt_convergence.svg", width: 100%),
  ),
  caption: [
    Left: the standard normal density. Right: standardized binomial densities converging toward the same bell curve.
  ],
)

== Summary

The normal law arises because addition smooths randomness, standardization removes location and scale, and the only stable finite-variance limit is Gaussian. That is why it appears so often in statistics, physics, measurement error, and natural variation.
