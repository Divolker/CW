def best_friend(txt, a, b):
    for i in txt:
        if a+b and not a+' '+b in txt and a!=b and a!=txt[0] and a!=txt[-1] and b!=txt[0] and b!=txt[-1]: c = True
        else:c = False
    return c
print(best_friend("a test", "t", "e"))