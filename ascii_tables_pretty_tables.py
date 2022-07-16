from prettytable import PrettyTable

# specify the column names while
# initializing the table
myTable = PrettyTable(["Student Name", "Class", "Percentage"])

# add rows
myTable.add_rows([["Yogesh", "X", "90.2%"],
	["Alex", "X", "87.5%"],
	["Vishal", "X", "90.23%"],
	["Rohan", "X", "92.7%"]
])

print(myTable)