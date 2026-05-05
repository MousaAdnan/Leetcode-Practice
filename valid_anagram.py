def isAnagram(s: str, t: str) -> bool:
    if s == "" or t == "":
        return False
    elif len(s) != len(t):
        return False
    

    for l in s:
        if l in t:
            t = t.replace(l,"", 1)
        else:
            return False
        
    return True
        

def main():
    s = "racecar"
    t = "carrace"
    a = isAnagram(s,t)
    print(a)

if __name__ == "__main__":
    main()