with open("problems/t1_2.txt", "r") as f:
    s = f.readlines()

def prob(s:list)-> int:
    d = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,
          "nine":9, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
    n = []
    nums = ["o", "t", "f", "s", "e", "n"]
    for i in range(1,10):
        nums.append(str(i))
    for l in s:
        t=[]
        for index,e in enumerate(l):
            pos=[]
            temp=[]
            for i in d.keys():
                if i in l[index:]:
                    pos.append(l[index:].index(i))
                    temp.append(d[i])
            if pos == []:
                continue
            else:
                t.append(temp[pos.index(min(pos))])
        n.append((t[0]*10)+t[-1])
    # print(n)
    return sum(n)

if __name__ == "__main__":
    print(prob(s))