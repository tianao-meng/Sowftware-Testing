import glob, os
import re
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.stats import pearsonr



addr = os.getcwd()+'/NRA'
#paths = sorted(Path(addr).iterdir(), key=os.path.getmtime)# sort files in modified time order



answerset = ["sat", "unsat", "timeout"]

#construct_dic_real_cvc4 = dict((['neg', 0], ['+', 0], ['-', 0], ['*', 0], ['/', 0],  ['<=', 0], ['<', 0],['>=', 0], ['>', 0]))

num_construct_cvc4_real_neg = []
num_construct_cvc4_real_plus = []
num_construct_cvc4_real_minus = []
num_construct_cvc4_real_mul = []
num_construct_cvc4_real_div = []
num_construct_cvc4_real_le = []
num_construct_cvc4_real_l = []
num_construct_cvc4_real_ge = []
num_construct_cvc4_real_g = []
time_cvc4_real = []

z3_no_err_file = []
cvc4_no_err_file = []
def drop_error_file_z3():
	for filename in os.listdir(addr):
		#print("filename: ",filename)
		with open(os.path.join(addr, filename), 'r') as f:
			lines = f.readlines()
			z3answer = re.sub("\n","", lines[8].split("> ")[1])
			if (z3answer == 'err'):
				continue
			else:
				z3_no_err_file.append(filename)

def drop_error_file_cvc4():

	for filename in os.listdir(addr):

		with open(os.path.join(addr, filename), 'r') as f:
			lines = f.readlines()
			cvc4answer = re.sub("\n","", lines[5].split("> ")[1])

			if (cvc4answer == 'err'):
				continue
			else:
				cvc4_no_err_file.append(filename)


#construct_dic_real_z3 = dict((['neg', 0], ['+', 0], ['-', 0], ['*', 0], ['/', 0],  ['<=', 0], ['<', 0],['>=', 0], ['>', 0]))
def update_construct_dic_cvc4_real():

	for filename in cvc4_no_err_file:

		with open(os.path.join(addr, filename), 'r') as f:
			construct_dic_real_cvc4 = dict((['neg', 0], ['+', 0], ['-', 0], ['*', 0], ['/', 0], ['<=', 0], ['<', 0], ['>=', 0], ['>', 0]))
			lines = f.readlines()
			cvc4time = float(lines[4].split("> ")[1])
			time_cvc4_real.append(cvc4time)

			find_formula_start = 0

			for line in lines:
				line = line.split(" ")
				if (line[0] != '(assert'):
					find_formula_start += 1


				if (line[0] == '(check-sat)\n'):
					find_formula_start -= 1

				if (line[0] == '(exit)\n'):
					find_formula_start -= 1
			print("find_formula_start: ",find_formula_start)
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
								construct_dic_real_cvc4['neg'] += 1
								flag_neg = 1
								break
							else:
								continue
						if (flag_neg == 0):
							construct_dic_real_cvc4['-'] += 1
							continue

				construct_dic_real_cvc4['+'] += line.count('(+')
				construct_dic_real_cvc4['*'] += line.count('(*')
				construct_dic_real_cvc4['/'] += line.count('(/')
				construct_dic_real_cvc4['<='] += line.count('(<=')
				construct_dic_real_cvc4['<'] += line.count('(<')
				construct_dic_real_cvc4['>='] += line.count('(>=')
				construct_dic_real_cvc4['>'] += line.count('(>')

			num_construct_cvc4_real_neg.append(construct_dic_real_cvc4['neg'])
			num_construct_cvc4_real_plus.append(construct_dic_real_cvc4['+'])
			num_construct_cvc4_real_minus.append(construct_dic_real_cvc4['-'])
			num_construct_cvc4_real_mul.append(construct_dic_real_cvc4['*'])
			num_construct_cvc4_real_div.append(construct_dic_real_cvc4['/'])
			num_construct_cvc4_real_le.append(construct_dic_real_cvc4['<='])
			num_construct_cvc4_real_l.append(construct_dic_real_cvc4['<'])
			num_construct_cvc4_real_ge.append(construct_dic_real_cvc4['>='])
			num_construct_cvc4_real_g.append(construct_dic_real_cvc4['>'])






# def update_construct_dic_cvc4_real():
#
# 	for filename in os.listdir(addr):
#
# 		with open(os.path.join(addr, filename), 'r') as f:
# 			lines = f.readlines()
# 			cvc4time = float(lines[4].split("> ")[1])
# 			cvc4answer = re.sub("\n","", lines[5].split("> ")[1])
# 			z3time = float(lines[7].split("> ")[1])
# 			z3answer = re.sub("\n","", lines[8].split("> ")[1])
# 			if (z3answer == 'unknown') or (cvc4answer == 'unknown'):
# 				print(filename)
		




if __name__ == "__main__":
	drop_error_file_z3()
	drop_error_file_cvc4()
	update_construct_dic_cvc4_real()

	# num_construct_z3_real_neg.append(construct_dic_real_z3['neg'])
	# num_construct_z3_real_plus.append(construct_dic_real_z3['+'])
	# num_construct_z3_real_minus.append(construct_dic_real_z3['-'])
	# num_construct_z3_real_mul.append(construct_dic_real_z3['*'])
	# num_construct_z3_real_div.append(construct_dic_real_z3['/'])
	# num_construct_z3_real_le.append(construct_dic_real_z3['<='])
	# num_construct_z3_real_l.append(construct_dic_real_z3['<'])
	# num_construct_z3_real_ge.append(construct_dic_real_z3['>='])
	# num_construct_z3_real_g.append(construct_dic_real_z3['>'])
	print ("num_construct_z3_real_neg: ",num_construct_cvc4_real_neg)
	print ("num_construct_z3_real_plus: ", num_construct_cvc4_real_plus)
	print ("num_construct_z3_real_minus: ", num_construct_cvc4_real_minus)
	print ("num_construct_z3_real_mul: ", num_construct_cvc4_real_mul)
	print ("num_construct_z3_real_div: ", num_construct_cvc4_real_div)
	print ("num_construct_z3_real_le: ", num_construct_cvc4_real_le)
	print ("num_construct_z3_real_l: ", num_construct_cvc4_real_l)
	print ("num_construct_z3_real_ge: ", num_construct_cvc4_real_ge)
	print ("num_construct_z3_real_g: ", num_construct_cvc4_real_g)
	print("time_z3_real: ",time_cvc4_real)
	print("no error files len: ", len(time_cvc4_real))
	score = []
	pccs_neg = pearsonr(num_construct_cvc4_real_neg, time_cvc4_real)
	print("pccs_neg_real_cvc4: ",pccs_neg)
	pccs_plus = pearsonr(num_construct_cvc4_real_plus, time_cvc4_real)
	print("pccs_plus_real_cvc4: ", pccs_plus)
	pccs_minus = pearsonr(num_construct_cvc4_real_minus, time_cvc4_real)
	print("pccs_minus_real_cvc4: ", pccs_minus)
	pccs_mul = pearsonr(num_construct_cvc4_real_mul, time_cvc4_real)
	print("pccs_mul_real_cvc4: ", pccs_mul)
	pccs_div = pearsonr(num_construct_cvc4_real_div, time_cvc4_real)
	print("pccs_div_real_cvc4: ", pccs_div)
	pccs_le = pearsonr(num_construct_cvc4_real_le, time_cvc4_real)
	print("pccs_le_real_cvc4: ", pccs_le)
	pccs_l = pearsonr(num_construct_cvc4_real_l, time_cvc4_real)
	print("pccs_l_real_cvc4: ", pccs_l)
	pccs_ge = pearsonr(num_construct_cvc4_real_ge, time_cvc4_real)
	print("pccs_ge_real_cvc4: ", pccs_ge)
	pccs_g = pearsonr(num_construct_cvc4_real_g, time_cvc4_real)
	print("pccs_g_real_cvc4: ", pccs_g)

	res_dic = {}
	res_dic["real_cvc4_neg"] = pccs_neg
	res_dic["real_cvc4_plus"] = pccs_plus
	res_dic["real_cvc4_minus"] = pccs_minus
	res_dic["real_cvc4_mul"] = pccs_mul
	res_dic["real_cvc4_div"] = pccs_div
	res_dic["real_cvc4_le"] = pccs_le
	res_dic["real_cvc4_l"] = pccs_l
	res_dic["real_cvc4_ge"] = pccs_ge
	res_dic["real_cvc4_g"] = pccs_g

	res = sorted(res_dic.items(), key=lambda x: x[1], reverse=True)
	str_to_print_1 = "{}{} {}".format('first', ':', [res[0][0]])
	str_to_print_2 = "{}{} {}".format('second', ':', [res[1][0]])
	str_to_print_3 = "{}{} {}".format('third', ':', [res[2][0]])
	print(str_to_print_1)
	print(str_to_print_2)
	print(str_to_print_3)
	#plt.scatter(num_construct_cvc4_real_neg, time_cvc4_real, alpha=0.6)
	#plt.show()