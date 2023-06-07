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


## Implementing the Object Oriented Design 

class Stock_Model:
    
    ## will take in a ticker 
    ## take in the time 

    pass


class basic_trace(Stock_Model): 

    def __init__(self, ticker_symbol: str, start_date: str, end_date: str, function_trace: str):
        self._ticker = ticker_symbol
        self._start = start_date 
        self._end = end_date
        self._function = function_trace
    
    def plot_function(self): 

        if self._function == "exponential":
            Ticker = self._ticker
            security = yf.Ticker(Ticker)
            start = self._start
            end = self._end 
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

        elif self._function == "trigonometric":

            Ticker = self._ticker
            security = yf.Ticker(Ticker)
            start = self._start
            end = self._end
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

        elif self._function == "logarithmic":
        
            Ticker = self._ticker
            security = yf.Ticker(Ticker)
            start = self._start
            end = self._end
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

        else:
            print("Invalid Entry of Function")
            print("Valid Entries: exponential, trigonometric and logarithmic")



graph_btc = basic_trace("BTC", "2019-01-01","2023-01-01","exponential")
graph_btc 










