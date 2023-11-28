def Hello(input):
    x = input
    x = x.replace(":)","🙂")
    x = x.replace(":(","🙁")
    return x

print(Hello(input()))

