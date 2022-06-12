import pandas as pd
import matplotlib.pyplot as plt
import os


pd.set_option("display.width", None)
FILES_DIR = os.getcwd()

# data to use | used ICMarkets data
path = "data/testing_GBPUSD_M15.csv"


def main():
    # Main plots

    # Main metrics and info

    # Volatility during day
        # metrics & analysis

    # Seasonal & overall tendencies
        # during year
        # during month
        # during week
        # during day

    # Other analysis ?
        # ...

    print('Done')

    return


def rename_data(data):
    data.rename(
        columns={"<DATE>": "date", "<TIME>": "time", "<OPEN>": "open", "<HIGH>": "high", "<LOW>": "low",
                 "<CLOSE>": "close",
                 "<TICKVOL>": "tick_vol", "<VOL>": "vol", "<SPREAD>": "spread"}, inplace=True)
    return data


def drop_columns(df):
    df.drop(columns=['open', 'high', 'low', 'close', 'spread', 'tick_vol', 'vol'], inplace=True)

    return df


def create_base_data():
    data_path = os.path.join(FILES_DIR, path)
    data = pd.read_csv(data_path, sep='\t')
    data = rename_data(data)

    return data


if __name__ == '__main__':
    main()
