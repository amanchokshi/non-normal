# non-normal
Generate a non-normal distributions with given a mean, variance, skewness and kurtosis using
the [Fleishman Method](https://link.springer.com/article/10.1007/BF02293811),
essentially a cubic transformation on a standard normal [X~N(0, 1)]

$$
Y =a +bX +cX^2 +dX^3
$$

where the coefficients ($a, b, c, d$) are tuned to create a distribution
with the desired statistic

![Non-Normal Distribution](https://raw.githubusercontent.com/amanchokshi/non-normal/main/docs/imgs/banner.png)
Figure 1. A non-normal field generated in the `usage` section below. The title
shows the input parameters, and the emperically measured statistics of the 
generated distribution

### Installation

Installs cleanly with a single invocation of the standard Python package tool:

```
$ pip install non-normal
```

### Usage

```
from non_normal import fleishman

# Input parameters for non-normal field
mean = 0
var = 1
skew = 1
ekurt = 2
size = 2**20

# Create an instance of the Fleishman class
ff = fleishman.Fleishman(mean=mean, var=var, skew=skew, ekurt=ekurt, size=size)

# Generate the field
ff.gen_field()
non_normal_data = ff.field

# Measure the stats of the generated samples
ff.field_stats

>>> {'mean':    0.000203128504124, 
     'var':     1.001352686678266, 
     'skew':    1.005612915524984, 
     'ekurt':   2.052527629375554,}
```

### References

1. [A method for simulating non-normal distributions](https://link.springer.com/article/10.1007/BF02293811)
2. [Functions for Simulating Data by Using Fleishman’s Transformation](https://support.sas.com/content/dam/SAS/support/en/books/simulating-data-with-sas/65378_Appendix_D_Functions_for_Simulating_Data_by_Using_Fleishmans_Transformation.pdf)
3. [Generation of Non-normal Data – A Study of Fleishman’s Power Method](https://www.diva-portal.org/smash/get/diva2:407995/FULLTEXT01.pd)
4. [Computing the real solutions of Fleishman's equations for simulating non-normal data](https://pubmed.ncbi.nlm.nih.gov/34779511/)
5. [Simulating multivariate nonnormal distributions](https://link.springer.com/article/10.1007/BF02293687)
6. [https://gist.github.com/zeimusu/7432603b85dc6406c6ea](https://gist.github.com/zeimusu/7432603b85dc6406c6ea)
