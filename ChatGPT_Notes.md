This is a **discrete-time signal**:

$$
x[n]=\left(\frac12\right)^n u[n]
$$

Let’s break it down:

* $x[n]$ → the signal, where $n$ is an integer (…, −2, −1, 0, 1, 2, …).
* $\left(\frac12\right)^n$ → an exponentially decaying sequence.
* $u[n]$ → the **unit-step signal**:

$$
u[n]=
\begin{cases}
1,&n\ge 0\\
0,&n<0
\end{cases}
$$

Therefore,

$$
x[n]=
\begin{cases}
0,&n<0\\
\left(\frac12\right)^n,&n\ge0
\end{cases}
$$

### So the actual values are:

| $n$ | $x[n]$ |
| ----: | -------: |
|    −2 |        0 |
|    −1 |        0 |
|     0 |    $1$ |
|     1 |  $1/2$ |
|     2 |  $1/4$ |
|     3 |  $1/8$ |
|     4 | $1/16$ |

So it looks like:

$$
\boxed{1,\frac12,\frac14,\frac18,\frac1{16},\ldots}
$$

starting at $n=0$, and it gets smaller and smaller.

**In simple words:** it's a **right-sided exponentially decaying signal**. The $u[n]$ is what makes the signal zero before $n=0$.
