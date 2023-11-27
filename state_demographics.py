import csv

file = open("state_demographics.csv")
data = list(csv.reader(file, delimiter=","))
print(data)
file.close()

State = []
Population = []
for i in range(len(data)):
    if data[i][1] != "-":
        State.append(data[i][0])
        Population.append(int(data[i][1]))
for i in range(len(State)):
    print(State[i] + " " + str(Population[i]))


