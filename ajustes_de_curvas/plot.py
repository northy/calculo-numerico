import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set(style='ticks')

def snsplot(xax, yax) :
    fig, ax = plt.subplots()

    ax.plot(xax, yax)
    
    ax.set_aspect('equal')
    ax.grid(True, which='both')
    sns.despine(ax=ax, offset=0)

def plot(xax, yax) :
    plt.figure(figsize=(6, 3), dpi=130)

    plt.plot(xax, yax)

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.show()

def plotrange(xax, yax, a, b) :
    plt.figure(figsize=(6, 3), dpi=130)

    plt.plot(xax, yax)

    ax = plt.gca()
    ylim = ax.get_ylim()

    plt.vlines(a, ylim[0], ylim[1], color='black')
    plt.vlines(b, ylim[0], ylim[1], color='black')

    plt.show()

def plotdot(xax, yax, dots) :
    plt.figure(figsize=(6, 3), dpi=130)

    plt.plot(xax, yax)

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    for dot in dots :
        plt.plot(dot[0], dot[1], 'ro')
    
    plt.show()
