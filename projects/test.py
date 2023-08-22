from tabulate import tabulate

while True:
    n = input("What multiples would you like to get? \n")
    table_data = []
    for i in range(0, 101):
        table_data.append([n, i, int(n) * i])
    
    table_headers = ["N", "Multiplier", "Result"]
    table = tabulate(table_data, headers=table_headers, tablefmt="grid")
    print(table)
