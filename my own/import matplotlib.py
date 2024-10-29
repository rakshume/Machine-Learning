import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import yfinance as yf

meta=yf.Ticker('meta')

stockinfo=meta.info

for key,value in stockinfo.items():
    print(key,":",value)