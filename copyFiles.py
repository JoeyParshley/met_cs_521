import shutil
SRC = 'template.py'
PREFIX = "jparshle@bu.edu_hw_5_"
EXT = ".py"

problems = ['10.7','10.9','11.7','11.11','14.3','14.11']

for problem in problems:
	filename = PREFIX + problem.replace('.','_') + EXT
	shutil.copy2(SRC,filename)
	print('{} copied to {}'.format(SRC, filename))
