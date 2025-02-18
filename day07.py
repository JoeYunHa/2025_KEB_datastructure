def a(i):
    j = 9
    print(i,j)

def b(k):
    a(1)
    print(k)

def main():
    print("start")
    b(3)



if __name__ == "__main__":
    main()