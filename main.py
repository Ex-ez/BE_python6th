def disp(sh):
    print("Disp Function")
    return sh


def show():
    return "Show Function"


r_sh = disp(show)
print(r_sh())
print(show())
