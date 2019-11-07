import random

__author__ = 'Khashayar'
__email__ = 'khashayarghamati@gmail.com'

import numpy as np
import matplotlib.pyplot as plt


class Statistics(object):

    def __init__(self, omega_set):
        self.omega_set = omega_set

    def is_sigma_field(self, sigma_set):
        if [] in sigma_set and self.omega_set in sigma_set:

            for element in sigma_set:
                c = self.get_complement(omega, element)
                if not c in sigma_set:
                    return False
                else:
                    el = set(element)
                    c_set = set(c)
                    u = list(el.union(c_set))

                    if not u in sigma_set:
                        return False
                    else:
                        inter = list(el.intersection(c_set))

                        if not inter in sigma_set:
                            return False

            return True

    def get_complement(self, omega, element):

        temp = []
        for e in element:
            temp.append(e)
        return list(set(omega) - set(temp))

    def is_rv_valid(self, rv, sigma):
        if self.is_sigma_field(sigma_set=sigma):
            for idx, value in enumerate(rv):
                if value[0] in self.omega_set:
                    riverse_idx = self.get_same_indices(rv, value[1])
                    if not riverse_idx in sigma:
                        return False
                else:
                    return False
            return True
        return False

    def get_same_indices(self, rv, value):
        result = [x[0] for i, x in enumerate(rv) if x[1] == value]

        for i in result:
            rv.remove((i, value))

        return result

    def draw_plot_of_distribution_function(self,
                                           rv,
                                           sigma_field):

        if (self.is_sigma_field(sigma_set=sigma_field) and
                self.is_rv_valid(rv.copy(), sigma_field)):

            rv_value = sorted([x[1] for x in rv])
            probability = sorted([random.random() for e in rv_value])

            x = np.array(rv_value)
            y = np.array(probability)

            plt.step(x, y, )
            plt.plot(x, y, 'C0o', alpha=0.5)
            plt.show()


if __name__ == '__main__':
    omega = [1, 2, 3]
    sigma = [
        [1],
        [2, 3],
        [1, 2, 3],
        []
    ]

    rv = [
        (1, 3),  # that's mean: X(1)=3
        (2, 4),  # that's mean: X(2)=4
    ]

    s = Statistics(omega_set=omega)

    print("1 -> check sigma field")
    print("2 -> check random variable")
    print("3 -> drew distribution function")

    c = int(input("Choose an item: "))

    r = None

    if c == 1:
        r = s.is_sigma_field(sigma_set=sigma)
    elif c == 2:
        r = s.is_rv_valid(rv, sigma)
    elif c == 3:
        s.draw_plot_of_distribution_function(
            rv=rv,
            sigma_field=sigma
        )
    else:
        print("command is not valid")

    if r is True:
        print("yes, it is")

    elif r is not None and not r:
        print("no, it is not")
