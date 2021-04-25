import csv
import pandas as pd


def save_individual(fit, cromossome):
    with open('../files/individuals.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([fit, cromossome])


def get_csv():
    data = pd.read_csv('../files/individuals.csv')
    inds = data.values.tolist()
    return inds
