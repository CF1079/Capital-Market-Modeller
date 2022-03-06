#dependencies
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
import pandas as pd
import numpy as np
import math as math
from time import sleep
from art import tprint
from scipy.optimize import curve_fit
from scipy.odr import ODR, Model, Data, RealData
from gekko import GEKKO
from numpy import sin
from numpy import sqrt
from numpy import log
from sklearn.metrics import r2_score
from numpy import exp
import datetime
from IPython.display import display, Image
from PIL import Image
import requests



def start_menu():
 tprint("Stock Modeler!")
 print("************************************************************************************************")
 print("\n Copyright © of Charlie Falk, 2021")
 print("\n Built for the IA1 Mathematical Methods PSMT")
 print("\n************************************************************************************************")
 sleep(1)
 print("Here are your options: \n [e] = Exponential \n [l] = Logarithmic \n [t] = Trigonometric")
 sleep(0.7)
 choosing = (input("\n What do you need???: "))
 while choosing != 'e' and choosing != 'l' and choosing != 't':
     print('Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n Incorrect Response! \n')
     sleep(0.3)
     print('Please Try Again')
     sleep(0.4)
     print("\n Here are your options: \n \n \n [e] = Exponential \n [l] = Logarithmic \n [t] = Trigonometric (sin and cos)")
     choosing = (input("\n What do you need???: "))
 if(choosing == 'e'):
     print('\n\nYour Choice Is >>> Exponential')
     Exponential_Menu()
 elif(choosing == 'l'):
     print('\n\nYour Choice Is >>> Logarthimic')
     Logarithmic_Menu()

 elif(choosing == 't'):
     print('\n\nYour Choice Is >>> Trigonometric')
     Trigonometric_Menu()

def Exponential_Menu():
    Ticker = input("\nTicker Symbol: ")
    security = yf.Ticker(Ticker)
    start = input("Start Date yyyy-mm-dd: ")
    end = input("End Date yyyy-mm-dd: ")
    df = security.history(start=f"{start}", end=f"{end}")
    close_price = df['Close'].to_list()
    time = [i for i in range(1, len(close_price) + 1)]



    # define the true objective function
    def objective(x, a, b, c, d):
        return a * (exp(b*(x+c)))+d

    x = time
    y = close_price


    # curve fit
    popt, _ = curve_fit(objective, x, y,maxfev=5000)
    # summarize the parameter values
    a,b,c,d = popt

    # plot input vs output
    plt.scatter(x, y,label="Observed Price Action")
    # define a sequence of inputs between the smallest and largest known inputs
    x_line = np.arange(min(x), max(x), 1)
    # calculate the output for the range
    y_line = objective(x_line, a, b, c, d)
    # create a line plot for the mapping function
    plt.plot(x_line, y_line, '--', color='red',label="Modeled Price Action")
    plt.xlabel("Time (Days Since Open)")
    plt.ylabel("Close Price")
    plt.title(f"Graph of {Ticker} Price Action from {start} to {end} ")
    plt.legend()
    print("\nGenerating Graph....")
    sleep(1)
    print("\nExit Graph to Continue!")
    sleep(2)
    plt.show()
    print("\nParameters: ")
    print(f"a = {a}\nb = {b}\nc = {c}\nd = {d}")
    sleep(1)
    print(f"\nRsquared: \n{r2_score(close_price[1:],y_line)}")
    sleep(1)
    print(f"\nEquation:\ny = {a}e^({b}*(x+{c}))+{d}")
    exit_menu()

def Trigonometric_Menu():
    Ticker = input("\nTicker Symbol: ")
    security = yf.Ticker(Ticker)
    start = input("Start Date yyyy-mm-dd: ")
    end = input("End Date yyyy-mm-dd: ")
    df = security.history(start=f"{start}", end=f"{end}")
    close_price = df['Close'].to_list()
    time = [i for i in range(1, len(close_price) + 1)]



    # define the true objective function
    def objective(x, a, b, c, d):
        return a * sin(b*(x+c))+d

    x = time
    y = close_price


    # curve fit
    popt, _ = curve_fit(objective, x, y,maxfev=5000)
    # summarize the parameter values
    a,b,c,d = popt

    # plot input vs output
    plt.scatter(x, y,label="Observed Price Action")
    # define a sequence of inputs between the smallest and largest known inputs
    x_line = np.arange(min(x), max(x), 1)
    # calculate the output for the range
    y_line = objective(x_line, a, b, c, d)
    # create a line plot for the mapping function
    plt.plot(x_line, y_line, '--', color='red',label="Modeled Price Action")
    plt.xlabel("Time (Days Since Open)")
    plt.ylabel("Close Price")
    plt.title(f"Graph of {Ticker} Price Action from {start} to {end} ")
    plt.legend()
    print("\nGenerating Graph....")
    sleep(1)
    print("\nExit Graph to Continue!")
    sleep(2)
    plt.show()
    print("\nParameters: ")
    print(f"a = {a}\nb = {b}\nc = {c}\nd = {d}")
    sleep(1)
    print(f"\nRsquared: \n{r2_score(close_price[1:],y_line)}")
    sleep(1)
    print(f"\nEquation:\ny = {a}sin({b}(x+{c}))+{d}")
    exit_menu()

def Logarithmic_Menu():
    Ticker = input("\nTicker Symbol: ")
    security = yf.Ticker(Ticker)
    start = input("Start Date yyyy-mm-dd: ")
    end = input("End Date yyyy-mm-dd: ")
    df = security.history(start=f"{start}", end=f"{end}")
    close_price = df['Close'].to_list()
    time = [i for i in range(1, len(close_price) + 1)]



    # define the true objective function
    def objective(x, a, b, c, d):
        return a * np.log(b*(x+c))+d

    x = time
    y = close_price


    # curve fit
    popt, _ = curve_fit(objective, x, y,maxfev=5000)
    # summarize the parameter values
    a,b,c,d = popt

    # plot input vs output
    plt.scatter(x, y,label="Observed Price Action")
    # define a sequence of inputs between the smallest and largest known inputs
    x_line = np.arange(min(x), max(x), 1)
    # calculate the output for the range
    y_line = objective(x_line, a, b, c, d)
    # create a line plot for the mapping function
    plt.plot(x_line, y_line, '--', color='red',label="Modeled Price Action")
    plt.xlabel("Time (Days Since Open)")
    plt.ylabel("Close Price")
    plt.title(f"Graph of {Ticker} Price Action from {start} to {end} ")
    plt.legend()
    print("\nGenerating Graph....")
    sleep(1)
    print("\nExit Graph to Continue!")
    sleep(2)
    plt.show()
    print("\nParameters: ")
    print(f"a = {a}\nb = {b}\nc = {c}\nd = {d}")
    sleep(1)
    print(f"\nRsquared: \n{r2_score(close_price[1:],y_line)}")
    sleep(1)
    print(f"\nEquation:\ny = {a}ln({b}(x+{c}))+{d}")
    exit_menu()

def exit_menu():
 sleep(1)
 print("\n\nWhere do you want to go? ")
 print("\n[m] = return to main menu \n[q] = quit")
 whats_next = input("\nWhere are you going now?: ")
 while whats_next != 'm' and whats_next != 'q':
    print('Incorrect Response! \n Incorrect Response! \n Incorrect Response!')
    sleep(0.3)
    print('Please Try Again')
    sleep(0.4)
    print("Where do you want to go? ")
    print("\n[m] return to main menu \n[q] quit")
    whats_next = (input("\nWhere are you going now?: "))
 if (whats_next == 'm'):
    start_menu()
 elif (whats_next == 'q'):
     print("\n HAVE A NICE DAY :)")
     sleep(2)
     import matplotlib.pyplot as plt
     import matplotlib.image as mpimg
     img = mpimg.imread('JOEL.png')
     imgplot = plt.imshow(img)
     print(imgplot)
     plt.show()

     quit()

start_menu()























