def outer():
    x_ = "local"

    def inner():
        nonlocal x_
        x_ = "nonlocal"
        print("inner:", x_)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x_)
    inner()
    print("outer:", x_)
    change_global()


x = "global"
print(x)
outer()
print(x)
