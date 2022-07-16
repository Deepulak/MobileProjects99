import wikipedia
# Extracting summary of an Article
summ = wikipedia.summary("Laptop")
print(summ)

# extracting 2line of sentence
summ = wikipedia.summary("Laptop", sentences=2)
print(summ)

# changing language
# print total language
print(wikipedia.languages())
# set language
#wikipedia.set_lang("hi")
# hi for hindi

data = wikipedia.summary("Laptop", sentences=4)
print(data)

# get search suggestion
data3 = wikipedia.suggest('laptops')
print(data3)

# access full page
data4 = wikipedia.page("Computer")
print(data4)

