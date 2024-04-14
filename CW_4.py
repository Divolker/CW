def warn_the_sheep(queue):
    for x in queue:
        v=queue[::-1]
        if x== "wolf":
            s=v.index(x)
        else:
            continue
        if v.index(x)==0:
            print ("'Pls go away and stop eating my sheep'")
        else:
            c="'Oi! Sheep number н! You are about to be eaten by a wolf!'"
            x=c.replace("н",str(s))
            print (x)
    return s
print(warn_the_sheep(["sheep", "sheep", "sheep", "wolf", "sheep", "sheep"]))