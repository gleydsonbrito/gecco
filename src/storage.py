import csv


def save_individual(ind):
    with open('ind.cvs', 'w', newline='') as file:
        write = csv.writer(file)
        write.writerow(['Fitness', 'Cromossome'])
        write.writerow(['João', 'g@Joao.com'])
