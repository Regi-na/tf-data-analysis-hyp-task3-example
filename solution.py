import pandas as pd
import numpy as np
from scipy import stats

chat_id = 947352272 # Ваш chat ID, не меняйте название переменной

def solution(cnt: np.array, test: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return stats.ttest_ind(cnt, test).pvalue < 0.03
