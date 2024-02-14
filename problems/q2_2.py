with open("problems/t2_1.txt", "r") as f:
    s = f.readlines()

def prob(s:list)-> int:
    n=[]
    for index,l in enumerate(s):
        d = l.split(": ")
        d = d[-1].split(" ")
        l = len(d)//2
        r=[]
        g=[]
        b=[]
        for i in range(l):
            if "red" in d[(2*i)+1]:
                r.append(int(d[2*i]))
            if "green" in d[(2*i)+1]:
                g.append(int(d[2*i]))
            if "blue" in d[(2*i)+1]:
                b.append(int(d[2*i]))
        else:
            # print(r,g,b)
            n.append((max(r) * max(g)) * max(b))
    return sum(n)

if __name__ == "__main__":
    print(prob(s))