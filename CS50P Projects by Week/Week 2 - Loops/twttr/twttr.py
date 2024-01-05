def main():
    tweet = input("Input: ")
    print(shorten(tweet))#, sep = "", end = "")

def shorten(t):
    i = 0
    shortened_word = ""
    while i in range(0, len(t)):
        for l in t:
            if l.lower() in ["a", "e", "i", "o", "u"]:
                l = ""
                #print(l,sep="",end="")
            elif l.lower():
                shortened_word += l
                #print(l,sep="",end="")
        return shortened_word


main()