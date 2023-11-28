def main():
    ans= input("Greeting ")
    print(f"${value(ans)}")



def value(greeting):
    ans = greeting.strip().lower()
    if ans[0:5] == "hello" :
        return 0
    elif ans[0] == "h" :
        return 20
    else :
        return 100


if __name__ == "__main__":
    main()