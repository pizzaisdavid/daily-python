import itertools

def main():
    numberOfGrades = 2
    raw = '385'
    highest = 0
    indexCombinations = itertools.combinations(range(len(raw)), numberOfGrades - 1)

    for indices in indexCombinations:
        grades = []
        for listPosition, index in enumerate(indices):
            previousIndexIndex = listPosition - 1
            previousIndex = 0
            if previousIndexIndex > 0:
                previousIndex = indices[previousIndexIndex]
            
            grades.append(raw[previousIndex:index + 1])

        lastIndex = indices[-1]
        notInclusive = lastIndex + 1
        grades.append(raw[notInclusive:])
        
        grades = [int(g) for g in grades if g != '']

        if len(grades) == numberOfGrades:
            print('- {} -'.format(indices))
            print(grades)
            average = sum(grades) / len(grades)
            if average > highest:
                highest = average
    print(highest)

if __name__ == '__main__':
    main()
