import csv
import pandas as pd


def save_individual(fit, cromossome):
    with open('/Users/gleydsonbrito/Documents/gecco/files/individuals.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([fit, cromossome])


def get_csv():
    inds = []
    data_frame = pd.read_csv(
        '/Users/gleydsonbrito/Documents/gecco/files/individuals.csv')
    for i in data_frame.values.tolist():
        float_cromossome = []
        fitness = float(i[0][1:-2])
        extracted_cromossome = i[1][1:-1]
        string_cromossome = extracted_cromossome.split(sep=',')
        for c in string_cromossome:
            float_cromossome.append(float(c.strip()))

        inds.append([fitness, float_cromossome])

    return inds
