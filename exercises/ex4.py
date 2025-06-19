def eh_3_5_15():
    # note that the interval for the loop is [1, 101)
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('cincisprezece')
        elif i % 3 == 0:
            print('trei')
        elif i % 5 == 0:
            print('cinci')
        else:
            print(i)

def eh_3_5_15_while():
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print('cincisprezece')
        elif i % 3 == 0:
            print('trei')
        elif i % 5 == 0:
            print('cinci')
        else:
            print(i)
        i += 1

def eh_3_5_15_listcomp():
    results = [
        'cincisprezece' if i % 3 == 0 and i % 5 == 0
        else 'trei' if i % 3 == 0
        else 'cinci' if i % 5 == 0
        else i
        for i in range(1, 101)
    ]
    for item in results:
        print(item)

def eh_3_5_15_map():
    def check(i):
        if i % 3 == 0 and i % 5 == 0:
            return 'cincisprezece'
        elif i % 3 == 0:
            return 'trei'
        elif i % 5 == 0:
            return 'cinci'
        else:
            return i
    for item in map(check, range(1, 101)):
        print(item)

def main():
    print("----- Using for loop:")
    eh_3_5_15()
    print("\n----- Using while loop:")
    eh_3_5_15_while()
    print("\n----- Using list comprehension:")
    eh_3_5_15_listcomp()
    print("\n----- Using map:")
    eh_3_5_15_map()

if __name__ == '__main__':
    main()