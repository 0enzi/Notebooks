numbers = []

# Collatz Conjecture (3n+1) The unsolvable math problem
def conjecture(n):
    n = int(n)
    count = 0
    numbers.append(n)

    # while n !=1:
    while count != 100:
        if n%2 == 0:
            count += 1
            n =n/2
            print("Number", n, "was even. Dividing by 2 [n/2]")
            numbers.append(n)

        else:
            count+=1
            n =n*3+1
            print("Number", n, "was odd. Dividing by 2 [3n+1]")
            numbers.append(n)


    print("It took",count, "Steps")
    print("NNNNN" , numbers)

h = input()
conjecture(h)