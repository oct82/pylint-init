
def get_volumes():
    return 'abc'

def get_other_volumes():
    return [i / 12 for i in range(3)]

def do_something(x):
    print(x)

def do_something_else(x):
    print(x)

for volume in get_volumes():
    do_something(volume)

for volme in get_other_volumes():
    do_something_else(volume)


print('-' * 20)

list_of_printers = []

for i in [1, 2, 3]:
    def printer():
        print(i)
    list_of_printers.append(printer)

for func in list_of_printers:
    func()
