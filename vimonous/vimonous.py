import subprocess as sub
import os

from typing import Union

class Vimonous:
	#helper keys
	ESC="\x1B"
	LF="\n"
	CR="\r"
	ENTER="\n"

	def __init__(self, filen: str="", data: str="", vim: str="vim", tmp: str=".venom.tmp", autosave: bool=True) -> None:
		self.filen=filen

		#instance of vim to use, ie vim, vim.gtk, gvim, etc
		self.vim_name=vim

		#filename of temporary file
		self.tmp_file=tmp

		#data to type into file
		self.inject=data

		#when true (default), the file will be auto saved when ran
		self.autosave=autosave

		#if constructor called with data set, auto run and save that data
		if self.inject:
			self.run()

	#given a filename, create the string to quit and save
	def save(self, filen: str=None) -> Union[str]:
		if filen:
			#save will force save filen and quit
			#should be called last
			return self.ESC+":wq! "+filen+self.ENTER

		elif self.filen:
			#if filen is not set, use filen from constructor
			return self.ESC+":wq! "+self.filen+self.ENTER

	#add data to data list when using + operator
	def add(self, data: str="") -> None:
		self.inject+=data

	#implicitly call add()
	def __add__(self, data: str="") -> None:
		self.add(data)

	#create temp file, execute vim, delete file
	def run(self) -> None:
		with open(self.tmp_file, "w") as f:
			#when autosave is on, add save command to end
			if self.autosave:
				self.add(self.save())

			f.write(self.inject)

		#open vim and save file
		sub.call([
			self.vim_name,
			"-s",
			self.tmp_file,
			self.filen
		])

		os.remove(self.tmp_file)

	def __call__(self) -> None:
		self.run()