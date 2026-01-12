MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score 
Agents = []
for i in range(MAX_N):
    Agents.append(Agent(codenames[i], scores[i]))
min_score = Agents[0].score
min_code = Agents[0].codename
n = len(Agents)
for i in range(n):
    if Agents[i].score <= min_score:
        min_score = Agents[i].score
        min_code = Agents[i].codename

print(min_code, min_score)

