import pandas as pd
import os

BASE_PATH = "../../../../local_data/jheaton/"
DATA_PATH = BASE_PATH + "class_10_2_lstm_sunspots/"
OUTPUT_PATH = BASE_PATH + "class_10_2_lstm_sunspots/"

os.system("mkdir -p " + OUTPUT_PATH)


names = [
    "year",
    "month",
    "day",
    "dec_year",
    "sn_value",
    "sn_error",
    "obs_num",
    "unused1",
]
# datafile = "https://data.heatonresearch.com/data/t81-558/SN_d_tot_V2.0.csv"
datafile = DATA_PATH+"SN_d_tot_V2.0.csv"
df = pd.read_csv(
    datafile,
    sep=";",
    header=None,
    names=names,
    na_values=["-1"],
    index_col=False,
)
print("Starting file:")
print(df[0:10])
print("Ending file:")
print(df[-10:])
