class Agent:
    def __init__(self, code_name=0, score=0):
        self.code_name = code_name
        self.score = score

agents = []
for _ in range(5):
    code_name, score = input().split()
    agents.append(Agent(code_name, int(score)))

idx = 0
for i in range(1,5):
    if agents[i].score < agents[idx].score:
        idx = i

print(agents[idx].code_name, agents[idx].score)