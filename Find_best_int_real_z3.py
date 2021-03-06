import glob, os
import re
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.stats import pearsonr



addr1 = os.getcwd()+'/NIRA1'
addr2 = os.getcwd()+'/NIRA2'
#paths = sorted(Path(addr).iterdir(), key=os.path.getmtime)# sort files in modified time order



answerset = ["sat", "unsat", "timeout"]




num_construct_z3_int_real_neg = []
num_construct_z3_int_real_plus = []
num_construct_z3_int_real_minus = []
num_construct_z3_int_real_mul = []
num_construct_z3_int_real_div = []
num_construct_z3_int_real_mod = []
num_construct_z3_int_real_rem = []
num_construct_z3_int_real_le = []
num_construct_z3_int_real_l = []
num_construct_z3_int_real_ge = []
num_construct_z3_int_real_g = []
time_z3_int_real = []


z3_no_err_file_1 = []
cvc4_no_err_file_1 = []
z3_no_err_file_2 = []
cvc4_no_err_file_2 = []

def drop_error_file_z3():
	for filename in os.listdir(addr1):
		#print("filename: ",filename)
		with open(os.path.join(addr1, filename), 'r') as f:
			lines = f.readlines()
			z3answer = re.sub("\n","", lines[8].split("> ")[1])
			if (z3answer == 'err'):
				continue
			else:
				z3_no_err_file_1.append(filename)

def drop_error_file_cvc4():

	for filename in os.listdir(addr1):

		with open(os.path.join(addr1, filename), 'r') as f:
			lines = f.readlines()
			cvc4answer = re.sub("\n","", lines[5].split("> ")[1])

			if (cvc4answer == 'err'):
				continue
			else:
				cvc4_no_err_file_1.append(filename)


#construct_dic_real_z3 = dict((['neg', 0], ['+', 0], ['-', 0], ['*', 0], ['/', 0],  ['<=', 0], ['<', 0],['>=', 0], ['>', 0]))
def update_construct_dic_z3_int_real():

	for filename in z3_no_err_file_1:

		with open(os.path.join(addr1, filename), 'r') as f:
			construct_dic_int_real_z3 = dict((['neg', 0], ['+', 0], ['-', 0], ['*', 0], ['div', 0], ['mod', 0], ['rem', 0], ['<=', 0],['<', 0], ['>=', 0], ['>', 0]))
			lines = f.readlines()
			z3time = float(lines[7].split("> ")[1])
			time_z3_int_real.append(z3time)
			#print("z3time: ",z3time)

			find_formula_start = 0

			for line in lines:
				line = line.split(" ")
				if (line[0] != '(assert'):
					find_formula_start += 1


				if (line[0] == '(check-sat)\n'):
					find_formula_start -= 1

				if (line[0] == '(exit)\n'):
					find_formula_start -= 1
			#print("find_formula_start: ",find_formula_start)
			lines = lines[find_formula_start:]
			for line in lines:
				line = line.split(" ")
				#print(line)
				for index in range(len(line)):

					if(line[index] == '(-'):
						flag_neg = 0
						for char in (line[index + 1]):
							#print(char)
							if (char == ')'):
								construct_dic_int_real_z3['neg'] += 1
								flag_neg = 1
								break
							else:
								continue
						if (flag_neg == 0):
							construct_dic_int_real_z3['-'] += 1
							continue

				construct_dic_int_real_z3['+'] += line.count('(+')
				construct_dic_int_real_z3['*'] += line.count('(*')
				construct_dic_int_real_z3['div'] += line.count('(div')
				construct_dic_int_real_z3['mod'] += line.count('(mod')
				construct_dic_int_real_z3['rem'] += line.count('(rem')
				construct_dic_int_real_z3['<='] += line.count('(<=')
				construct_dic_int_real_z3['<'] += line.count('(<')
				construct_dic_int_real_z3['>='] += line.count('(>=')
				construct_dic_int_real_z3['>'] += line.count('(>')

			num_construct_z3_int_real_neg.append(construct_dic_int_real_z3['neg'])
			num_construct_z3_int_real_plus.append(construct_dic_int_real_z3['+'])
			num_construct_z3_int_real_minus.append(construct_dic_int_real_z3['-'])
			num_construct_z3_int_real_mul.append(construct_dic_int_real_z3['*'])
			num_construct_z3_int_real_div.append(construct_dic_int_real_z3['div'])
			num_construct_z3_int_real_mod.append(construct_dic_int_real_z3['mod'])
			num_construct_z3_int_real_rem.append(construct_dic_int_real_z3['rem'])
			num_construct_z3_int_real_le.append(construct_dic_int_real_z3['<='])
			num_construct_z3_int_real_l.append(construct_dic_int_real_z3['<'])
			num_construct_z3_int_real_ge.append(construct_dic_int_real_z3['>='])
			num_construct_z3_int_real_g.append(construct_dic_int_real_z3['>'])


def drop_error_file_z3_1():
	for filename in os.listdir(addr2):
		#print("filename: ",filename)
		with open(os.path.join(addr2, filename), 'r') as f:
			lines = f.readlines()
			z3answer = re.sub("\n","", lines[8].split("> ")[1])
			if (z3answer == 'err'):
				continue
			else:
				z3_no_err_file_2.append(filename)

def drop_error_file_cvc4_1():

	for filename in os.listdir(addr2):

		with open(os.path.join(addr2, filename), 'r') as f:
			lines = f.readlines()
			cvc4answer = re.sub("\n","", lines[5].split("> ")[1])

			if (cvc4answer == 'err'):
				continue
			else:
				cvc4_no_err_file_2.append(filename)


#construct_dic_real_z3 = dict((['neg', 0], ['+', 0], ['-', 0], ['*', 0], ['/', 0],  ['<=', 0], ['<', 0],['>=', 0], ['>', 0]))
def update_construct_dic_z3_int_real_1():

	for filename in z3_no_err_file_2:

		with open(os.path.join(addr2, filename), 'r') as f:
			construct_dic_int_real_z3 = dict((['neg', 0], ['+', 0], ['-', 0], ['*', 0], ['div', 0], ['mod', 0], ['rem', 0], ['<=', 0],['<', 0], ['>=', 0], ['>', 0]))
			lines = f.readlines()
			z3time = float(lines[7].split("> ")[1])
			time_z3_int_real.append(z3time)
			#print("z3time: ",z3time)

			find_formula_start = 0

			for line in lines:
				line = line.split(" ")
				if (line[0] != '(assert'):
					find_formula_start += 1


				if (line[0] == '(check-sat)\n'):
					find_formula_start -= 1

				if (line[0] == '(exit)\n'):
					find_formula_start -= 1
			#print("find_formula_start: ",find_formula_start)
			lines = lines[find_formula_start:]
			for line in lines:
				line = line.split(" ")
				#print(line)
				for index in range(len(line)):

					if(line[index] == '(-'):
						flag_neg = 0
						for char in (line[index + 1]):
							#print(char)
							if (char == ')'):
								construct_dic_int_real_z3['neg'] += 1
								flag_neg = 1
								break
							else:
								continue
						if (flag_neg == 0):
							construct_dic_int_real_z3['-'] += 1
							continue

				construct_dic_int_real_z3['+'] += line.count('(+')
				construct_dic_int_real_z3['*'] += line.count('(*')
				construct_dic_int_real_z3['div'] += line.count('(div')
				construct_dic_int_real_z3['mod'] += line.count('(mod')
				construct_dic_int_real_z3['rem'] += line.count('(rem')
				construct_dic_int_real_z3['<='] += line.count('(<=')
				construct_dic_int_real_z3['<'] += line.count('(<')
				construct_dic_int_real_z3['>='] += line.count('(>=')
				construct_dic_int_real_z3['>'] += line.count('(>')

			num_construct_z3_int_real_neg.append(construct_dic_int_real_z3['neg'])
			num_construct_z3_int_real_plus.append(construct_dic_int_real_z3['+'])
			num_construct_z3_int_real_minus.append(construct_dic_int_real_z3['-'])
			num_construct_z3_int_real_mul.append(construct_dic_int_real_z3['*'])
			num_construct_z3_int_real_div.append(construct_dic_int_real_z3['div'])
			num_construct_z3_int_real_mod.append(construct_dic_int_real_z3['mod'])
			num_construct_z3_int_real_rem.append(construct_dic_int_real_z3['rem'])
			num_construct_z3_int_real_le.append(construct_dic_int_real_z3['<='])
			num_construct_z3_int_real_l.append(construct_dic_int_real_z3['<'])
			num_construct_z3_int_real_ge.append(construct_dic_int_real_z3['>='])
			num_construct_z3_int_real_g.append(construct_dic_int_real_z3['>'])

if __name__ == "__main__":
	drop_error_file_z3()
	drop_error_file_cvc4()
	update_construct_dic_z3_int_real()
	drop_error_file_z3_1()
	drop_error_file_cvc4_1()
	update_construct_dic_z3_int_real_1()

	# num_construct_z3_real_neg.append(construct_dic_real_z3['neg'])
	# num_construct_z3_real_plus.append(construct_dic_real_z3['+'])
	# num_construct_z3_real_minus.append(construct_dic_real_z3['-'])
	# num_construct_z3_real_mul.append(construct_dic_real_z3['*'])
	# num_construct_z3_real_div.append(construct_dic_real_z3['/'])
	# num_construct_z3_real_le.append(construct_dic_real_z3['<='])
	# num_construct_z3_real_l.append(construct_dic_real_z3['<'])
	# num_construct_z3_real_ge.append(construct_dic_real_z3['>='])
	# num_construct_z3_real_g.append(construct_dic_real_z3['>'])
	print ("num_construct_z3_int_real_neg: ",num_construct_z3_int_real_neg)
	print ("num_construct_z3_int_real_plus: ", num_construct_z3_int_real_plus)
	print ("num_construct_z3_int_real_minus: ", num_construct_z3_int_real_minus)
	print ("num_construct_z3_int_real_mul: ", num_construct_z3_int_real_mul)
	print ("num_construct_z3_int_real_div: ", num_construct_z3_int_real_div)
	print ("num_construct_z3_int_real_rem: ", num_construct_z3_int_real_rem)
	print ("num_construct_z3_int_real_mod: ", num_construct_z3_int_real_mod)
	print ("num_construct_z3_int_real_le: ", num_construct_z3_int_real_le)
	print ("num_construct_z3_int_real_l: ", num_construct_z3_int_real_l)
	print ("num_construct_z3_int_real_ge: ", num_construct_z3_int_real_ge)
	print ("num_construct_z3_int_real_g: ", num_construct_z3_int_real_g)
	print("time_z3_int_real: ",time_z3_int_real)
	print("no error files len: ", len(time_z3_int_real))
	score = []
	pccs_neg = pearsonr(num_construct_z3_int_real_neg, time_z3_int_real)
	print("pccs_neg_int_real_z3: ",pccs_neg)
	pccs_plus = pearsonr(num_construct_z3_int_real_plus, time_z3_int_real)
	print("pccs_plus_int_real_z3: ", pccs_plus)
	pccs_minus = pearsonr(num_construct_z3_int_real_minus, time_z3_int_real)
	print("pccs_minus_int_real_z3: ", pccs_minus)
	pccs_mul = pearsonr(num_construct_z3_int_real_mul, time_z3_int_real)
	print("pccs_mul_int_real_z3: ", pccs_mul)
	pccs_div = pearsonr(num_construct_z3_int_real_div, time_z3_int_real)
	print("pccs_div_int_real_z3: ", pccs_div)
	pccs_mod = pearsonr(num_construct_z3_int_real_mod, time_z3_int_real)
	print("pccs_mod_int_real_z3: ", pccs_mod)
	pccs_rem = pearsonr(num_construct_z3_int_real_rem, time_z3_int_real)
	print("pccs_rem_int_real_z3: ", pccs_rem)
	pccs_le = pearsonr(num_construct_z3_int_real_le, time_z3_int_real)
	print("pccs_le_int_real_z3: ", pccs_le)
	pccs_l = pearsonr(num_construct_z3_int_real_l, time_z3_int_real)
	print("pccs_l_int_real_z3: ", pccs_l)
	pccs_ge = pearsonr(num_construct_z3_int_real_ge, time_z3_int_real)
	print("pccs_ge_int_real_z3: ", pccs_ge)
	pccs_g = pearsonr(num_construct_z3_int_real_g, time_z3_int_real)
	print("pccs_g_int_real_z3: ", pccs_g)

	res_dic = {}
	res_dic["int_real_z3_neg"] = pccs_neg
	res_dic["int_real_z3_plus"] = pccs_plus
	res_dic["int_real_z3_minus"] = pccs_minus
	res_dic["int_real_z3_mul"] = pccs_mul
	res_dic["int_real_z3_div"] = pccs_div
	res_dic["int_real_z3_mod"] = pccs_mod
	# res_dic["int_z3_rem"] = pccs_rem
	res_dic["int_real_z3_le"] = pccs_le
	res_dic["int_real_z3_l"] = pccs_l
	res_dic["int_real_z3_ge"] = pccs_ge
	res_dic["int_real_z3_g"] = pccs_g

	res = sorted(res_dic.items(), key=lambda x: x[1], reverse=True)
	print(res)
	str_to_print_1 = "{}{} {}".format('first', ':', [res[0][0]])
	str_to_print_2 = "{}{} {}".format('second', ':', [res[1][0]])
	str_to_print_3 = "{}{} {}".format('third', ':', [res[2][0]])
	print(str_to_print_1)
	print(str_to_print_2)
	print(str_to_print_3)

	#plt.scatter(num_construct_z3_int_real_neg, time_z3_int_real, alpha=0.6)
	#plt.show()