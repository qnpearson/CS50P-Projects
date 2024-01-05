def main():
    file = input("What is your file?").lower()
    if ext(file) == "jpg" or ext(file) == "jpeg":
        print("image/jpeg")
    elif ext(file) == "gif":
        print("image/gif")
    elif ext(file) == "png":
        print("image/png")
    elif ext(file) == "pdf":
        print("application/pdf")
    elif ext(file) == "txt":
        print("text/plain")
    elif ext(file) == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")

def ext(f):
    if ".jpg" in f or ".jpeg" in f:
        return "jpg"
    elif ".gif" in f:
        return "gif"
    elif ".png" in f:
        return "png"
    elif ".pdf" in f:
        return "pdf"
    elif ".txt" in f:
        return "txt"
    elif ".zip" in f:
        return "zip"
main()