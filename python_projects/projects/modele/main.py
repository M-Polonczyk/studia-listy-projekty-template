from Classes import LotkaVolterra, Lorenz, wahadeuko

wahadeuko(10)
wahadeuko(20)
wahadeuko(30)
# Model = LotkaVolterra()
# Model.start_sympy()
# Model.start_ode()

# Lorenz1 = Lorenz()
# Lorenz1.start_sympy()


'''
def lotka(a=1.2, b=0.6, c=0.3, d=0.8, x0=2, y0=1, t=25, dt=0.001):
    t = np.arange(0, t+dt, dt)
    x = [x0]
    y = [y0]
    for i in range(int(t[-1]/dt)):
        x.append(x[i] + dt * (a - b*y[i])*x[i])
        y.append(y[i] + dt * (c*x[i] - d)*y[i])
    return t, x, y

t, x, y = lotka()

plt.plot(t, x, label='prey')
plt.plot(t, y, label='predator')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Model Lotki-Volterry')
plt.legend()
plt.show()
'''
