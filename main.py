from PUI.flet import *
# AND FOR AUTO RELOAD WHEN YOU SAVE FILE
# use reloadium
import reloadium


# AND I CREATE STATE FOR DATA COUNTER
data = State()



# AND NOW I CREATE APP 
class FMyApp(FApplication):
	def __init__(self):
		super().__init__()
		# NOW I CREATE COUNTER STATE IN HERE
		data.counter:int  = 0
		# AND NOW FOR YOU USE TEXTFIELD INPUT 
		# YOU CAN BINDING DATA FROM HERE
		data.mytext:str = "hello PUI"


	# AND NOW I CREATE COUNTER WITH 2 BUTTON and text
	def content(self):
		# i CREATE WINDOW WITH TITLE AND SIZE WINDOW
		with FWindow(title="you app flet",size=(330,500)):
			# AND CREATE COLUMN
			with FColumn():
				# AND CREATE ROW
				with FRow():
					# AND I CREATE BUTTON INCREMENT
					FElevatedButton("-").click(self.min),
					FText(data.counter),
					FElevatedButton("+").click(self.add),

				with FRow():
					FText(data.mytext),
					FTextField(data("mytext"))



	# FOR DECREMENT BUTTON
	def min(self):
		data.counter -= 1
	# For INCREMENT
	def add(self):
		data.counter += 1

# reloadium: after_reload
def after_reload():
	PUIView.reload()

root = FMyApp()
root.run()