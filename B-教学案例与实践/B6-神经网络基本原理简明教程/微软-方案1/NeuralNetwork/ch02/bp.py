import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = 2
    y = 2.13
    while(True):
        print("forward...")
        # forward
        a = x*x
        b = np.log(a)
        c = np.sqrt(b)
        print(x,a,b,c)
        print("backward...")
        # backward
        loss = c - y
        if np.abs(loss) < 0.001:
            break
        delta_c = loss
        delta_b = delta_c * 2 * np.sqrt(b)
        delta_a = delta_b * a
        delta_x = delta_a / 2 / x
        x = x - delta_x
        print(delta_c, delta_b, delta_a, delta_x)

    print(x,a,b,c,loss)
    x = np.linspace(1,10)
    a = x*x
    b = np.log(a)
    c = np.sqrt(b)
    plt.plot(x,c)
    plt.show()
