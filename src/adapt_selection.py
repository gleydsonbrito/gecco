from deap import tools
from constants import NPOP


# def rank_selection(pop):
#     ranked_list = sorted(pop, key=lambda i: i[0], reverse=True)
#     best_individual = ranked_list[-1]
#     extracted_best = ranked_list[:-1]
#     print(extracted_best)


# rank_selection([[82.20345, [6.454345937492587, 10.034157708822725, 6.859570538756065, 3.834792121889387, 6.347686167432631, 6.605141602373866, 3.395743079249614, 5.354139619925853, 32.44214022444632, 22.33280189865792, 4.52973612230098, 6.7233090336645445, 1.2621511756425665, 0.07192095532851389, 0.08369086141984908, 0.005285721054101872, 0.12118247878682095, 0.001950276156324264, 0.10991024411332019, 0.26087555798894235, 0.1144524918846552, 0.5522596342477135, 0.007853779405719838, 2.725783023076529, 1.0727100531469653, 0.04819612753031851, 1.07762439403926, 3.9154702467681277, 0.5624720513391546]], [65.43627, [12.289222853791898, 11.67926741300714, 3.269762526310391, 3.1451363226325064, 3.034887661736478, 8.311107772901261, 4.638132084747473, 3.100799457555526, 32.97006385650336, 17.117281021687578, 3.2843960878514387, 2.638709648472697, 1.872779715950783, 0.05935156209837136, 0.08549634479131304,
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            0.009999263417047037, 0.10479905640156906, 0.0008033421182041021, 0.09031074628906427, 0.3397785905310565, 0.09866977604044949, 0.7759595072377761, 0.008558391662501073, 3.4287767003382323, 0.12707554347227462, 0.007320889827167166, 1.7481091312865678, 4.420218011439577, 0.5823539543498661]], [66.72561, [13.469324354049657, 10.237395236272262, 3.7776699440967714, 7.070946569608433, 4.73487708533564, 6.7481536030116835, 4.933407084361195, 5.787108385149551, 28.471201132069094, 23.872014750681565, 4.974116075970707, 5.253939345101637, 1.148200363438676, 0.05966011952066427, 0.09027285314543186, 0.015648906008966745, 0.08782240586071413, 0.000906774114371086, 0.10600992432278901, 0.3112369852405711, 0.09757815058274835, 0.6284477173582051, 0.0043625456429564275, 3.473702743224818, 0.042923342434252054, 0.04452411015718813, 1.660927251020536, 3.6451665800935733, 0.5785037354356554]]])

def ranking_selection(pop):
    k = len(pop)-2
    best_ind = tools.selBest(pop, 1)
    k_worst_individuals = tools.selWorst(pop, k)
    offspring = tools.selRoulette(k_worst_individuals, NPOP-1)

    return best_ind + offspring
