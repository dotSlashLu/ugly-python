def split_and_join():
    s = "a|b|c"
    print("original", s)
    l = s.split("|")
    print("splited", l)
    s1 = ",".join(l)
    print("joined", s1)

split_and_join()
