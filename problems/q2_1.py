with open("problems/t2_1.txt", "r") as f:
    s = f.readlines()

def prob(s:list, max_rgb:list)-> int:
    n=[]
    for index,l in enumerate(s):
        d = l.split(": ")
        d = d[-1].split(" ")
        l = len(d)//2
        for i in range(l):
            if ("red" in d[(2*i)+1]) and (int(d[2*i])>max_rgb[0]) :
                break
            elif ("green" in d[(2*i)+1]) and (int(d[2*i])>max_rgb[1]) :
                break
            elif ("blue" in d[(2*i)+1]) and (int(d[2*i])>max_rgb[2]) :
                break
        else:
            n.append(index+1)
    return sum(n)

if __name__ == "__main__":
    r = int(input("No. of red cubes: "))
    g = int(input("No. of green cubes: "))
    b = int(input("No. of blue cubes: "))
    print(prob(s, [r,g,b]))