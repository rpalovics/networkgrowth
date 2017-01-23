import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
import math

class Plot:

  def set(self,font_scale = 2):
    sns.set(font="Droid Sans",font_scale = font_scale)
    sns.set_style("whitegrid")
    sns.set_color_codes("dark")
    sns.set_palette("Paired",10)
