import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

    df = pd.read_csv('D:/pascucci2.csv', encoding = 'cp949')

    if platform.system() == 'Windows':
        matplotlib.rc('font', family='Malgun Gothic')
    elif platform.system() == 'Darwin':
        matplotlib.rc('font', family='AppleGothic')
    else:
        matplotlib.rc('font', family='NanumGothic')

    def getlocal(x):
        return x.split(" ")[0]
    df['local'] = df['address'].apply(getlocal)

    
    df['local'].value_counts

    
    CountStatus = pd.value_counts(df['local'].values, sort=True)
    CountStatus.plot.bar()
    CountStatus.plot.bar(grid=True, figsize=(10,50), fontsize=5)
    plt.show()
    
    
    
    
    
