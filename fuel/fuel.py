res = 0
while True:
    try:
          inp = input("Fraction: ")
          tmp = inp.split("/")
          res = int(tmp[0]) / int(tmp[1])
    except (ValueError, ZeroDivisionError):
         continue
    else:
        if res <= 1 :
            if res >= 0.99 :
                 print("F")
            elif res <= 0.01 :
                 print("E")
            else :
                 print(f"{round(res * 100)}%")
            break