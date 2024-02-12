ext = input("what is extension? ")

if (".gif") in ext:
    print("image/gif")
elif (".jpeg") in ext:
    print("image/jpeg")
elif (".jpg") in ext:
    print("image/jpeg")
elif (".png") in ext:
    print("image/png")
elif (".pdf") in ext:
    print("application.pdf")
elif (".txt") in ext:
    print("text/plain")
elif (".zip") in ext:
    print("application/zip")
else:
    print("application/octet-stream")
