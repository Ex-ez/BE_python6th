def disp():
    def show():
        return "show Function"
    print("Disp Function")
    return show

r_sh = disp()
print(r_sh())