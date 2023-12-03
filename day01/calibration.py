
def calculate1(lines: list[str]):
    sum = 0
    for line in lines:
        first = None
        last = None
        for c in line:
            if not c.isdigit():
                continue
            if first is None:
                first = int(c)
            last = int(c)
        sum += (first * 10 + last)
    return sum

number_arr = [
    "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine",
]

def calculate2(lines: list[str]):
    def extract_numbers(line: str):
        p2 = 0
        first = None
        last = None
        for p1, char in enumerate(line):
            if (char.isdigit()):
                if first is None:
                    first = int(char)
                last = int(char)
                p2 = p1
            for n, s in enumerate(number_arr):
                if s in line[p2: p1+1]:
                    if first is None:
                        first = n + 1
                    last = n + 1
                    p2 = p1
        return first, last
    sum = 0
    for line in lines:
        first, last = extract_numbers(line)
        #print(first * 10 + last)
        sum += (first * 10 + last)
    return sum

if __name__ == "__main__":
    with open("calibration_doc.txt", "r") as doc:
        lines: list[str] = doc.readlines()
        sum1 = calculate1(lines)
        print(sum1)

        sum2 = calculate2(lines)
        print(sum2)
