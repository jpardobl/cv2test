g = [{"uno": "unno"},{"dos": "doos"}]


def show(t):
    print t

map(lambda e: show( "k %s v %s" % (key(e),e[key(e)])), g)
