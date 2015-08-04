import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)


#uniform

# plt.plot([0.0,1.0], [0.1, 0.1], 'k-', lw=2)
# plt.ylim([0.0,1.0])
# plt.show()

#beta
from scipy.stats import beta
a,b = 1.1,30
x = np.linspace(beta.ppf(0.00000000000000000001, a, b),
              beta.ppf(0.999999999999999999999, a, b), 10000)

plt.plot(x, beta.pdf(x, a, b),
         'r-', lw=4, alpha=0.6, label='beta pdf (a,b = 1.1,30)')
plt.xlim([0.0,1.0])
plt.show()