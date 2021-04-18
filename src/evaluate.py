import subprocess


def evaluate(candidateSolution):
    evalCommand = "docker run --rm mrebolle/r-geccoc:Track1 -c 'Rscript objfun.R "
    parsedCandidate = ",".join([str(x) for x in candidateSolution])
    evall = (subprocess.check_output(evalCommand +
                                     '"' + parsedCandidate + '"\'', shell=True))
    res = float(evall)
    return res,
