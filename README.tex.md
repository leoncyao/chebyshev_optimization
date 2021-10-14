# chebyshev_optimization

Let the supremum norm of a polynomial over the domain $I$ be given by 

||p(x)||_I = sup_{x \in I}{|p(x)|}

We want to find the polynomial the minimizes this norm. Formally, this means we want to solve the problem
$$
t_{\mathbb{Z}, n} = \min_{p \in \mathbb{Z}, p \neq 0\}||p(x)||_I^{1/n}
$$
where the optimal value for a given $n$ is denoted $t_{\mathbb{Z}, n}(I)$. 
We can then take the limit as $n \righarrow \infty$ and we will call this limit the \b{integer Chebyshev constant} denoted,

$$t_{\mathbb{Z}(I)} = \lim_{n \rightarrow \infty}{t_{\mathbb{Z}, n}(I)}

The chebyshev.py script uses the gurobi library to solve this problem. 

You can run 

python chebyshev.py

to calculate the optimum value of $n = 2$

TODO:
-Add cases n > 2
-Add option to increase n until value converges within given range

Hare, K. G. , & Hodges, P. W. . (Accepted). Applications of Integer and Semi-Infinite Programming to the Integer Chebyshev Problem. Experimental Mathematics. Retrieved from https://doi.org/10.1080/10586458.2019.1691089