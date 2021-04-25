import csv
import pandas as pd


def save_individual(fit, cromossome):
    with open('../files/individuals.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([fit, cromossome])


def get_csv():
    inds = []
    data_frame = pd.read_csv('files/individuals.csv')
    for i in data_frame.values.tolist():
        float_croms = []
        fit = float(i[0][1:7])
        final_pos = len(i[1])-1
        substring_croms = i[1][1:final_pos]
        string_croms = substring_croms.split(sep=',')
        for c in string_croms:
            float_croms.append(float(c.strip()))

        inds.append([fit, float_croms])

    return inds
