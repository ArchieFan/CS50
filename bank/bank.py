ans= input("Greeting ")
ans = ans.strip().lower()
if ans[0:5] == "hello" :
    print("$0")
elif ans[0] == "h" :
    print("$20")
else :
    print("$100")