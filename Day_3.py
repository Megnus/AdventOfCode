import re

f = open('Input/input_day_3.txt', 'r')
data = f.read()
f.close()

inputArray = data.splitlines()
digAndNullList = [re.split('[\W|x]', x) for x in inputArray]
digList = [list(filter(lambda x: x != '', x)) for x in digAndNullList]
intList = [[int(y) for y in x] for x in digList]

koordList = []
for x in intList:
    for i in range(x[1], x[1] + x[3]):
        for j in range(x[2], x[2] + x[4]):
            koordList.append([i, j])

print([True if koordList.count(x) > 1 else False  for x in koordList].count(True))

exit()

sortedData = [list(s) for s in inputArray]

sortedData = [sorted(list(s)) for s in data.splitlines()]
aggregatedData = []

for dataElement in sortedData:
    charContArray = [dataElement.count(x) for x in set(dataElement)]
    filteredList = list(filter(lambda x: x != 1, charContArray))
    flatList = [item for sublist in dataElement for item in sublist]
    [aggregatedData.append(x) for x in set(sorted(filteredList))]

countArray = [[x, aggregatedData.count(x)] for x in set(aggregatedData)]
result_1 = countArray[0][1] * countArray[1][1]

for i in range(0, len(sortedData) - 1):
    for j in range(i + 1, len(sortedData)):
        if [a == b for a, b in zip(sortedData[i], sortedData[j])].count(False) == 1:
            result_2 = ''.join([a if a == b else '' for a, b in zip(sortedData[i], sortedData[j])])

print(result_1, result_2)
