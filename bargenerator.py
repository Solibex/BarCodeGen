__version__ = 1.1
try:
    import random
    import requests
	import webbrowser
	from tkinter import messagebox
except ImportError:
    print('Failed to import')
    print('Contact to Solibez!')
def check_updates():
	try:
        # -- Online Version File
        # -- Replace the url for your file online with the one below.
		response = requests.get('https://raw.githubusercontent.com/Solibex/BarCodeGen/main/version.txt')
		data = response.text
		if float(data) > float(__version__):
			messagebox.showinfo('Software Update', 'Update Available!')
			webbrowser.open_new_tab()
		elif float(data) < float(__version__):
			messagebox.showinfo('Software check', 'Software is pro version!')
	except BufferError:
		print('No internet. or laggy internet')
check_updates()
print_times = 1
barcode_length = 20
def generatebarcode() -> str:
    return ''.join(random.choice(["I", "l"]) for _ in range(barcode_length))
print(generatebarcode())
