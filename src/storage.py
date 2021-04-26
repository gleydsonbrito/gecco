import csv
import pandas as pd


def save_individual(fit, cromossome):
    with open('../files/individuals.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([fit, cromossome])


def get_csv():
    inds = []
    data_frame = pd.read_csv('../files/individuals.csv')
    for i in data_frame.values.tolist():
        float_croms = []
        fitness = float(i[0][1:-2])
        extracted_croms = i[1][1:-1]
        string_croms = extracted_croms.split(sep=',')
        for c in string_croms:
            float_croms.append(float(c.strip()))

        inds.append([fitness, float_croms])

    return inds
