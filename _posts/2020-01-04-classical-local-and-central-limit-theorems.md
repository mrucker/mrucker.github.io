---
layout: post
---
In the history of probability theory there has been considerable thought devoted to describing the distribution for infinite sums of random variables. In this effort two classic approaches have been developed:

1. Local Limit Theorems
2. Central Limit Theorems

Each of these approaches contain many theorems with different assumptions. All of these theorems, in the classical understanding, prove that the limiting distribution (with the appropriate assumptions) is normal. (More recent work has applied central limit techniques to prove limiting distributions other than normal.) The primary difference between these approaches then is not their purpose or goal, but rather the technique used in proving the theorems. To demonstrate these differences we will consider two classic proofs for each family as presented in {% cite  gnedenko2018theory %}.

# Classical Theorems

## The Local Demoivre-Laplace Theorem

Given an i.i.d. sequence of Bernoulli random variables \\(\xi_1, \xi_2, \ldots,\xi_n\\) with \\(p\\) probability of success, \\(P_n(k) = \mathbf{P}\left(\sum_{i=1}^{n}\xi_i=k\right) \\) satisfies \\[ \lim_{n\to\infty} P_n(k) = \frac{1}{\sqrt{2\pi np(1-p)}} e^{\left(-x^2/2\right)}, \\] when \\(x\\) is bound to a finite interval and \\( x = \frac{k-np}{\sqrt{np(1-p)}} \\).

## Lindeberg's Central Limit Theorem

Given a sequence of random variables \\(\xi_1, \xi_2, \ldots,\xi_n\\) with finite variance and mean, \\(P_n(k) = \mathbf{P}\left(\frac{1}{\sigma}\sum_{i=1}^n\(\xi_i -\mathbf{E}\xi_i) = k \right) \\) satisfies \\[\lim_{n\to\infty} P_n(k) = \frac{1}{\sqrt{2\pi}} e^{\left(-k^2/2\right)}, \\] when \\( \lim_{n\to\infty}\frac{1}{\sigma^2}\sum_{i=1}^n\mathbf{E}\left[(\xi_i - \mathbf{E}\xi_i) \mathbf{1}\_{\vert\xi_i-\mathbf{E}\xi_i\vert > \tau\sigma} \right] \\), \\(\sigma^2=\mathbf{Var}(\sum_{i=1}^n\xi_i) \\) and \\(\tau > 0\\).


# The Difference

We can see above that the difference in the two approaches is simply how the distribution is centered and normalized. In the case of the central limit theorem all the random variables are centered to their mean and normed by the variance before the theorem begins. In the local theorem none of the variables are modified. Instead the variable \\(k\\) is modified into the quantity \\(x\\).

{% bibliography --cited %}
