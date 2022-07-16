import pyfiglet

data = pyfiglet.figlet_format("Python")
print(data)

data_data = pyfiglet.figlet_format("Python", font="digital")
print(data_data) 

# List of ascii art styles
fonts = pyfiglet.FigletFont.getFonts()
fonts = list(fonts)
print(len(fonts))