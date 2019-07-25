def method():
    print("Method of some module...")
    print(__name__)

if __name__ == "__main__":
    print("This is from main module")
else:
    print("This has been called from some other module")

