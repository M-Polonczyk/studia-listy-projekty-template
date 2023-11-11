import abc
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from sympy import Function, dsolve, Eq, symbols, plot
from sympy.solvers.ode.systems import dsolve_system


class _Differential(abc.ABC):

    def __init__(self, x0, y0, t, dt):
        self.x0 = x0
        self.y0 = y0
        self.t = t
        self.dt = dt
        self.t = np.arange(0, self.t + self.dt, self.dt)

    @abc.abstractmethod
    def f(self, x, y):
        pass

    @abc.abstractmethod
    def _append_lines(self, t, lines):
        pass

    @abc.abstractmethod
    def _draw(self, x):
        pass

    @abc.abstractmethod
    def _make_ode(self):
        pass

    @abc.abstractmethod
    def f_scipy(self, X0, t):
        pass

    def start(self):
        lines = np.zeros((int(self.t[-1] / self.dt) + 1, 3))
        lines[0, 0] = self.x0
        lines[0, 1] = self.y0
        lines = self._append_lines(self.t, lines)
        return self._draw(lines)

    def start_ode(self):
        return self._draw(self._make_ode())

    def aprx(self, lines):
        approx = []
        for i in range(int(self.t[-1] / self.dt)):
            approx.append(abs(lines[i] - lines[i+1]))
        return np.mean(approx)


class LotkaVolterra(_Differential):
    def __init__(self, x0=2, y0=1, a=1.2, b=0.6, c=0.3, d=0.8, t=25, dt=0.001):
        super().__init__(x0, y0, t, dt)

        # self.x0 = x0
        # self.y0 = y0
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        # self.t = t
        # self.dt = dt

    def f(self, x, y):
        dx_dt = x + self.dt * (self.a - self.b * y) * x
        dy_dt = y + self.dt * (self.c * x - self.d) * y
        return dx_dt, dy_dt

    def _append_lines(self, t, lines):
        for i in range(int(t[-1] / self.dt)):
            lines[i + 1, 0], lines[i + 1,
                                   1], = self.f(lines[i, 0], lines[i, 1])
        return lines

    def _draw(self, x):
        plt.plot(self.t, x[:, 0], label='prey', lw=0.7)
        plt.plot(self.t, x[:, 1], label='predator', lw=0.7)
        plt.xlabel('Time')
        plt.ylabel('Population')
        plt.title('Model Lotki-Volterry')
        plt.legend()
        plt.show()

    def _make_ode(self):
        return odeint(self.f_scipy, [self.x0, self.y0], self.t)

    def f_scipy(self, X0, t):
        return [X0[0] * (self.a - self.b * X0[1]), X0[1] * (self.c * X0[0] - self.d)]

    def start_sympy(self):
        t = symbols('t')
        x = Function('x')
        y = Function('y')
        a, b, c, d = 1.2, 0.6, 0.3, 0.8
        dx_dt = Eq(x(t).diff(t), (a - b * y(t))*x(t))
        dy_dt = Eq(y(t).diff(t), (c*x(t) - d)*y(t))
        dsolve_system([dx_dt, dy_dt],
        ics={x(0): 2, y(0): 1}
        )



class Lorenz(_Differential):

    def __init__(self, sigma=10, beta=8/3, rho=28, x0=1, y0=1, z0=1, t=25, dt=0.001):
        self.sigma = sigma
        self.beta = beta
        self.rho = rho

        self.z0 = z0
        self.t = t
        self.dt = dt
        self.t = np.arange(0, self.t + self.dt, self.dt)

    def f_scipy(self, X0, t):
        dx_dt = self.sigma * (X0[1] - X0[0])
        dy_dt = X0[0] * (self.rho - X0[2]) - X0[1]
        dz_dt = X0[1] * X0[0] - self.beta * X0[2]
        return [dx_dt, dy_dt, dz_dt]

    def f(self, x, y, z):
        dx_dt = x + self.dt * self.sigma * (y - x)
        dy_dt = y + self.dt * (self.rho * x - x * z - y)
        dz_dt = z + self.dt * (x * y - self.beta * z)
        return dx_dt, dy_dt, dz_dt

    def _append_lines(self, t, lines):
        approx = []
        lines[0, 2] = self.z0
        for i in range(int(t[-1] / self.dt)):
            lines[i + 1, 0], lines[i + 1, 1], lines[i + 1,
                                                    2] = self.f(lines[i, 0], lines[i, 1], lines[i, 2])
            approx.append(abs(lines[i] - lines[i+1]))
        print(np.mean(approx))
        return lines

    def _draw(self, lines):
        ax = plt.figure().add_subplot(projection='3d')
        ax.plot(*lines.T, lw=0.5)
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        ax.set_zlabel("Z Axis")
        ax.set_title("Lorenz Attractor")
        plt.show()
        self.__draw_2d(lines)

    def __whatever(self, x, y, xl, yl):
        plt.plot(x, y, lw=0.5)
        plt.xlabel(xl)
        plt.ylabel(yl)
        plt.title('Lorenz Attractor')
        plt.show()

    def __draw_2d(self, lines):
        self.__whatever(lines[:, 0], lines[:, 1], 'X', 'Y')
        self.__whatever(lines[:, 0], lines[:, 2], 'X', 'Z')
        self.__whatever(lines[:, 1], lines[:, 2], 'Y', 'Z')

    def _make_ode(self):
        return odeint(self.f_scipy, [self.x0, self.y0, self.z0], self.t)

    def start_sympy(self):
        t = symbols('t')
        x = Function('x')
        y = Function('y')
        z = Function('z')
        dx_dt = Eq(x(t).diff(t), self.sigma*(y(t) - x(t)))
        dy_dt = Eq(y(t).diff(t), x(t) * (self.rho - z(t)) - y(t))
        dz_dt = Eq(z(t).diff(t), x(t) * y(t) - self.beta*z(t))
        dsolve_system([dx_dt, dy_dt, dz_dt])


def wahadeuko(time):
    t = symbols('t')
    x = Function('x')
    k = 10
    plot(dsolve(Eq(x(t).diff(t, 2), -k*x(t)), ics={x(0): np.pi / 18, x(t).diff(t).subs(t, 0): 0}).rhs, (t, 0, time), axis_center=(-1, -0.2),
         title='Energia wahadełka')
