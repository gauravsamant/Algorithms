import pandas as pd
import numpy as np
import tensorflow as tf
import torch
import matplotlib.pyplot as plt
import seaborn as sns
import time
import random

# Constant Time Function
def take_first(my_list: list) -> list:
    return my_list[0]

short_list = [10, 13, 23]

tic = time.process_time()
first = take_first(short_list)
toc = time.process_time()

print(toc - tic)

