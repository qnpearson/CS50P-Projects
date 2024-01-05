def main():
    x = input("Here's your input:")
    print(playback(x))

def playback(n):
    return n.replace(" ", "...")

main()
