# Project Rocky Road
# Author: Gabriel Moretenson, Tristan Bailey
# DLM (Date Last Modified): 12/16/2022
# Desc:
#   Drive file for testing if the database hanlder pytohn object works as intended
#   for making bulk updats to the MongoDB. Code developed by Tristan and Gabriel.
# use libraries for CNNs and ML traning
import numpy as np
# from tensorflow import keras
# import tensorflow as tf
# import matplotlib.pyplot as plt
import csv
import requests
import pandas as pd
from dotenv import load_dotenv
import os

from Data_Manager import Data_Manager


def main():
    print("========Welcome to ROS Backend========")

    addPinData()


def addPinData():
    # Obtain the the data from CSV file
    df = pd.read_csv('src_con/Data.csv', usecols=[
        'Pid', 'Lattitude', 'Longitude', 'Altitude', 'MeasurementDate',
        'UploadDate', 'Source', 'Cid', 'Classification', 'Degree'])
    print(df)
    load_dotenv()
    data_manager = Data_Manager(
        os.environ["MONGOAPIUSER"], os.environ["MONGOAPIKEY"])

    # Add data to the database
    # Note Pins is a custom name for the connection (you can rename it)
    for index, row in df.iterrows():
        data_manager.add(row['Pid'], row['Lattitude'], row['Longitude'], row['Altitude'],
                         row['MeasurementDate'], row['UploadDate'], row['Source'], row['Cid'], row['Classification'], row['Degree'])

    data_manager.push()


# main guard
if __name__ == "__main__":
    main()
