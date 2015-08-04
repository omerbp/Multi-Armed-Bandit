import random

from matplotlib.pyplot import subplot, legend, xlabel, ylabel, semilogx, axis, show,plot, text

from beta_bandit import *

theta = (0.25, 0.35)

def is_conversion(title):
    if random.random() < theta[title]:
        return True
    else:
        return False

conversions = [0,0]
trials = [0,0]

N = 1000
trials = zeros(shape=(N,2))
successes = zeros(shape=(N,2))
choices = zeros(shape=(N,))

bb = BetaBandit()
for i in range(N):
    choice = bb.get_recommendation()
    choices[i] = choice
    conv = is_conversion(choice)
    bb.add_result(choice, conv)

    trials[i] = bb.trials
    successes[i] = bb.successes

n = arange(N)+1
ad1 = sum(choices)
ad0 = N-ad1



subplot(111)
semilogx(n, (successes[:,0]+successes[:,1])/n, label="CTR")
semilogx(n, zeros(shape=(N,))+0.35, label="Best CTR")
semilogx(n, zeros(shape=(N,))+0.30, label="Random chance CTR")
semilogx(n, zeros(shape=(N,))+0.25, label="Worst CTR")
axis([0,N,0.15,0.45])
xlabel("Number of trials")
ylabel("CTR")
legend(loc=2)
show()


subplot(111)
plot(n, choices,'r*')
text(10.4, 0.4,"Ad 0 : {0}\nAd 1 : {1}".format(int(ad0),int(ad1)),fontsize=18,color='b')
axis([0,N,-0.5,1.5])
legend(loc=2)
xlabel("Number of trials")
ylabel("Chosen Ad")
show()


subplot(111)
n = arange(N)+1
plot(n, trials[:,0], label="Ad 0")
plot(n, trials[:,1], label="Ad 1")
plot(n, arange(N)+1, label="diagonal")
legend()
xlabel("Number of trials")
ylabel("Number of trials/Ad")
legend(loc=2)
show()



