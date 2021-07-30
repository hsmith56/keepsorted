import glob, os, time

def move():
	for file in glob.glob('*.exe'):
		try:
			c = os.getcwd() + '\\' +(file)
			d = os.getcwd() + "\\EXE's\\" + file
			os.rename(c,d)
			print('Moved {} to {}'.format(file,d))
		except Exception as e:
			c = os.getcwd() + '\\' +(file)
			d = os.getcwd() + "\\EXE's\\" + file
			os.remove(c)
			# d = os.getcwd() + "\\EXE's\\" + '(1) ' + file
			# os.rename(c,d)
			print('Reoved duplicate of {}, file exists at {}'.format(file,d))

	for file in glob.glob('*.zip'):
		try:
			c = os.getcwd() + '\\' +(file)
			d = os.getcwd() + "\\ZIP's\\" + file
			os.rename(c,d)
			print('Moved {} to {}'.format(file,d))
		except Exception as e:
			c = os.getcwd() + '\\' +(file)
			d = os.getcwd() + "\\ZIP's\\" + '(1) ' + file
			os.rename(c,d)
			print('Moved {} to {}. Error encountered: {}'.format(file,d,e))

	for file in glob.glob('*.pdf'):
		try:
			c = os.getcwd() + '\\' +(file)
			d = os.getcwd() + "\\PDF's\\" + file
			os.rename(c,d)
			print('Moved {} to {}'.format(file,d))
		except Exception as e:
			c = os.getcwd() + '\\' +(file)
			d = os.getcwd() + "\\PDF's\\" + '(1) ' + file
			os.rename(c,d)
			print('Moved {} to {}. Error encountered: {}'.format(file,d,e))

	for file in glob.glob('*.py'):
		if file != 'keepsorted.py':
			try:
				c = os.getcwd() + '\\' +(file)
				d = os.getcwd() + "\\Python\\" + file
				os.rename(c,d)
				print('Moved {} to {}'.format(file,d))
			except Exception as e:
				c = os.getcwd() + '\\' +(file)
				d = os.getcwd() + "\\Python\\" + '(1) ' + file 
				os.rename(c,d)
				print('Moved {} to {}. Error encountered: {}'.format(file,d,e))

	for file in glob.glob('*.txt'):
			try:
				c = os.getcwd() + '\\' +(file)
				d = os.getcwd() + "\\TXT's\\" + file
				os.rename(c,d)
				print('Moved {} to {}'.format(file,d))
			except Exception as e:
				c = os.getcwd() + '\\' +(file)
				d = os.getcwd() + "\\TXT's\\" + '(1) ' + file
				os.rename(c,d)
				print('Moved {} to {}. Error encountered: {}'.format(file,d,e))

if __name__ == '__main__':
	try:
		os.makedirs("EXE's")
	except FileExistsError as e:
		print(e)

	try:
		os.makedirs("ZIP's")
	except FileExistsError as e:
		print(e)

	try:
		os.makedirs("PDF's")
	except FileExistsError as e:
		print(e)

	try:
		os.makedirs('Python')
	except FileExistsError as e:
		print(e)

	try:
		os.makedirs("TXT's")
	except FileExistsError as e:
		print(e)		


	try:
		while True:
			move()
			time.sleep(10)
	except KeyboardInterrupt:
		pass
