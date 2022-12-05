import pandas as pd
import numpy as np
from tqdm.auto import tqdm


def read_data_as_pd(url):
    return pd.read_csv(url)

def ashwins_shiz(dataset):
    # new_dataset = pd.DataFrame()
    
    # funcs = [np.mean, np.std, np.max, np.min]
    outs = dataset["Penicillin concentration(P:g/L)"]
    # print(outs)
    # print(dataset.keys())
    # dataset.drop(index = ['Penicillin concentration(P:g/L)'], inplace=True)
    dataset = dataset[dataset.columns.drop(list(dataset.filter(regex='Penicillin')))]

    mean = dataset.rolling(window=5).mean()
    mean = mean.add_suffix("_mean")
    std = dataset.rolling(window=5).std()
    std = mean.add_suffix("_std")
    maxx = dataset.rolling(window=5).max()
    maxx = mean.add_suffix("_max")
    minn = dataset.rolling(window=5).min()
    minn = mean.add_suffix("_min")

    new_df = pd.concat([mean, std, maxx, minn, pd.Series(outs)], axis=1)
    new_df.to_csv("ashwin_data.csv", index=False, sep=',')

    


        

    # new_dataset = pd.DataFrame(new_dataset)
    # new_dataset.to_csv("ashwin_data.csv", index=False, sep=',')

    return

if __name__ == "__main__":
    url = "clean_data.csv"
    ashwins_shiz(read_data_as_pd(url))
