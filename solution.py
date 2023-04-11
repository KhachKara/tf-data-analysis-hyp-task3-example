# https://github.com/Anastasiamay
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

chat_id = 42791670 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    alpha = 0.01
    t_stat, p_value = ttest_1samp(x, 300)
    return p_value/2 < alpha and t_stat < 0
