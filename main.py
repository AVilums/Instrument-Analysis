import pandas as pd
import matplotlib.pyplot as plt
import os

pd.set_option("display.width", None)
FILES_DIR = os.getcwd()

# data to use | used ICMarkets data
path = "data/testing_GBPUSD_M15.csv"


def main():

    plot_volatility_during_day_full()
    plot_volatility_during_day_tokyo_open()
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
    # create data path
    data_path = os.path.join(FILES_DIR, path)

    data = pd.read_csv(data_path, sep='\t')

    # rename column names
    data = rename_data(data)

    return data


def plot_volatility_during_day_full():
    # creating base data
    data = create_base_data()

    # times based on GMT+3
    df = pd.DataFrame(data)

    # TODO - better formula for volatility
    # (high - low)+(open - close) * n / 2
    df['volatility'] = ((df['high'] - df['low']) + (df['open'] - df['close'])) * 100 / 2

    # redo dataframe with time & volatility
    df = df[['time', 'volatility']].copy()

    time = df.loc[95:190, 'time']
    df = df.groupby(time).mean()

    # plot graph
    df.plot(title='Volatility during 24H',
            figsize=(16, 8), grid=True)

    plt.show()

    return


def plot_volatility_during_day_tokyo_open():
    # creating base data
    data = create_base_data()

    # times based on GMT+3
    df = pd.DataFrame(data)

    # TODO - better formula for volatility
    # (high - low)+(open - close) * n / 2
    df['volatility'] = ((df['high'] - df['low']) + (df['open'] - df['close'])) * 100 / 2

    # redo dataframe with time & volatility
    df = df[['time', 'volatility']].copy()

    # TODO - check validity
    # get daily times
    time = df.loc[95:190, 'time']

    # TODO - check math
    # average volatility per period
    df = df.groupby(time).mean()

    # TODO - check validity
    # drop rows before Tokyo sessions
    df = df.iloc[8:]

    # TODO - add line labels (london & ny open)
    # plot graph
    ax = df.plot(title="Volatility during 24H - starting Tokyo",
                 figsize=(16, 12), grid=True)
    ax.axvline(33, color='red', linestyle='--')
    ax.axvline(53, color='red', linestyle='--')
    plt.show()

    return


if __name__ == '__main__':
    main()
