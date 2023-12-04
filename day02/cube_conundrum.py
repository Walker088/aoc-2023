
RED_MAX=12
GREEN_MAX=13
BLUE_MAX=14

def quize_1(games: list[str]):
    sum = 0
    for i, g in enumerate(games):
        g = g.split(": ")[1:][0].split("; ")
        g = ", ".join(g).split(", ")
        red_cnt = 0
        green_cnt = 0
        blue_cnt = 0
        for r in g:
            num = int(r.split(" ")[0])
            if "red" in r and num > red_cnt:
                red_cnt = num
            if "green" in r and num > green_cnt:
                green_cnt = num
            if "blue" in r and num > blue_cnt:
                blue_cnt = num
        if (red_cnt <= RED_MAX and green_cnt <= GREEN_MAX and blue_cnt <= BLUE_MAX):
            sum += (i+1)
    return sum

def quize_2(games: list[str]):
    sum = 0
    for i, g in enumerate(games):
        g = g.split(": ")[1:][0].split("; ")
        g = ", ".join(g).split(", ")
        red_cnt = 0
        green_cnt = 0
        blue_cnt = 0
        for r in g:
            num = int(r.split(" ")[0])
            if "red" in r and num > red_cnt:
                red_cnt = num
            if "green" in r and num > green_cnt:
                green_cnt = num
            if "blue" in r and num > blue_cnt:
                blue_cnt = num
        sum += (red_cnt * green_cnt * blue_cnt)
    return sum

if __name__ == "__main__":
    with open("cube_conundrum_data_test_1.txt", "r") as doc:
        games: list[str] = doc.readlines()
        print(quize_1(games))
        print(quize_2(games))
        
    with open("cube_conundrum_data.txt", "r") as doc:
        games: list[str] = doc.readlines()
        print(quize_1(games))
        print(quize_2(games))
