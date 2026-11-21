__counter = 0

def summ(a_list):
    global __counter
    __counter += 1
    a_sum = 0
    for elem in a_list:
        a_sum += elem
    return a_sum

def product(a_list):
    global __counter
    __counter += 1
    prod = 1
    for elem in a_list:
        prod *= elem
    return prod

if __name__ == "__main__":
    print("Why are you running me?  I am a module, thank you very much.")
