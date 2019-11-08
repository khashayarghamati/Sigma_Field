__author__ = 'Khashayar'
__email__ = 'khashayarghamati@gmail.com'

import matplotlib.pyplot as plt
import numpy as np


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

        return result

    def draw_plot_of_distribution_function(self,
                                           rv,
                                           sigma_field,
                                           isEstimate=False):

        if (self.is_sigma_field(sigma_set=sigma_field) and
                self.is_rv_valid(rv.copy(), sigma_field)):

            rv_value = sorted([x[1] for x in rv])
            probability = sorted([1 / len(self.omega_set) for e in rv_value])
            sum_p = 0
            dis_p = []
            for i in probability:
                sum_p += i
                dis_p.append(sum_p)

            if not isEstimate:
                xmin = []
                xmax = []
                for i in range(len(rv_value)):
                    if i%2 == 0:
                        xmin.append(rv_value[i]-1)
                    else:
                        xmax.append(rv_value[i]-0.1)

                if len(xmin) != len(xmax):
                    if len(xmax)< len(xmin):
                        xmax.append(xmax[len(xmax)-1]+1)
                    else:
                        xmin.append(xmin[len(xmin)-1] + 1)

                xmin.append(xmin[len(xmin)-1]+1)
                xmax.append(xmax[len(xmax)-1]+1)
                fig, ax = plt.subplots(1, 1)
                ax.hlines(dis_p, xmin=xmin, xmax=xmax)
                plt.show()

            return rv_value, dis_p

        return None, None

    def draw_density(self, rv, probability):

        x = np.array(rv)
        y = np.array(probability)
        plt.plot(x, y, 'C0o', alpha=1)
        plt.show()

    def estimate_expected_value(self, rv, probability):
        expect = 0
        for i in range(len(rv)):
            expect += rv[0] * probability[0]

        return expect


if __name__ == '__main__':
    omega = [1, 2, 3]
    sigma = [
        [1],
        [2],
        [3],
        [1, 2],
        [1, 3],
        [2, 3],
        [1, 2, 3],
        []
    ]

    rv = [
        (1, 3),  # that's mean: X(1)=3
        (2, 4),  # that's mean: X(2)=4
        (3, 5),  # that's mean: X(3)=5
    ]

    s = Statistics(omega_set=omega)

    print("1 -> check sigma field")
    print("2 -> check random variable")
    print("3 -> draw distribution function")
    print("4 -> draw density function")
    print("5 -> estimate expect value")

    c = int(input("Choose an item: "))

    r = None
    sorted_rv, p = None, None

    if c == 1:
        r = s.is_sigma_field(sigma_set=sigma)
    elif c == 2:
        r = s.is_rv_valid(rv, sigma)
    elif c == 3:
        sorted_rv, p = s.draw_plot_of_distribution_function(
            rv=rv,
            sigma_field=sigma
        )
    elif c == 4:
        sorted_rv, p = s.draw_plot_of_distribution_function(
            rv=rv,
            sigma_field=sigma,
            isEstimate=True

        )
        if sorted_rv and p:
            s.draw_density(sorted_rv, p)
        else:
            print('R.V and P not found')
    elif c == 5:
        sorted_rv, p = s.draw_plot_of_distribution_function(
            rv=rv,
            sigma_field=sigma,
            isEstimate=True

        )
        if sorted_rv and p:
            expect = s.estimate_expected_value(sorted_rv, p)
            print(f"Expect Value is : {expect}")
    else:
        print("command is not valid")

    if r is True:
        print("yes, it is")

    elif r is not None and not r:
        print("no, it is not")
