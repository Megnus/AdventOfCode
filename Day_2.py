f = open('Input/input_day_2.txt', 'r')
data = f.read()
f.close()

inputArray = data.splitlines()
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
