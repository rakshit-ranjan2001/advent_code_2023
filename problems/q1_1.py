with open("problems/t1_1.txt", "r") as f:
    s = f.readlines()

def prob(s:list) -> int:
    n = []
    for l in s:
        t=0
        for i in l:
            if i.isnumeric():
                t = (t*10)+int(i)
        n.append(t)
    res = 0
    for i in n:
        res+=int(str(i)[0] + str(i)[-1])
    return res

if __name__ == "__main__":
    print(prob(s))