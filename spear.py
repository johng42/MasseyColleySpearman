'''Quick look to get Pearson coefficient of two lists'''

def loadTeam(fname):
    return [line.strip() for line in open(fname)]

def Spearman(m,c):
	#quick check to make sure the lists are the same length
    assert len(m) == len(c)
    #brute force search
    #could build a dictionary with ranks instead if perf is a concern
    sum = 0
    colleyIndex = 1
    for team in c:
        masseyIndex = 1
        for mteam in m:
            if mteam != team:#then this is not a match, so check next team
                masseyIndex+=1
            else:
                break
        sum+=(masseyIndex-colleyIndex)**2
        colleyIndex+=1
    n=len(c)
    spearmancoeff = float(1.0-(6.0*sum)/(n*(n**2-1)))
    return spearmancoeff

#these are the output of the octave scripts from the class
c= loadTeam('ColleyRanks.txt')
m = loadTeam('MasseyRanks.txt')

print "Spearman coefficient of the two lists is ",Spearman(m,c)