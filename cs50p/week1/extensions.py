def main():
    name = input("File name: ").strip().lower()

    if name.endswith(".jpg") | name.endswith(".jpeg"):
        return print("image/jpeg")
    elif name.endswith(".gif"):
        return print("image/gif")
    elif name.endswith(".png"):
        return print("image/png")
    elif name.endswith(".pdf"):
        return print("application/pdf")
    elif name.endswith(".txt"):
        return print("text/plain")
    elif name.endswith(".zip"):
        return print("application/zip")
    else:
        return print("application/octet-stream")

main()
