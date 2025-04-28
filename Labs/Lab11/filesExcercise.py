# Joshua Hamaker        04/04/2025
# Lab 11 - File Exercise


def main() -> None:
    IDs = getStudentInfo()
    # print(IDs)
    scores = {}
    for k in IDs.keys():
        scores[k] = []
    scores = getScoresInfo(scores)
    # print(scores)
    saveData(IDs, scores)



def getStudentInfo() -> dict[str, str]:
    outDict = {}
    with open("students.txt", "r") as f:
        for l in f:
            if not "ID" in l:
                line = l.split(",")
                outDict[line[0]] = line[1].strip()
    return outDict


def getScoresInfo(d: dict[str, list[float]]) -> dict[str, list[float]]:
    with open("scores.txt", "r") as f:
        for l in f:
            if not "ID" in l:
                line = l.split(",")
                d[line[0]].append(float(line[2]))
    return d


def saveData(students: dict[str, str], scores: dict[str, list[float]]) -> None:
    with open("grades.txt", "w") as f:
        f.write("Student ID, Name, Total Scores, Sum of All Scores, Score Average\n")
        for k in students.keys():
            line = f"{k}, {students[k]}, {len(scores[k])}, {sum(scores[k])}, {sum(scores[k])/len(scores[k])}\n"
            f.write(line)


if __name__ == '__main__':
    main()