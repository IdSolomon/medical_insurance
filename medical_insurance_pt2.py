# I will apply my newfound knowledge of Python functions to write a 
# useful function that calculates medical insurance costs.

# In this code, I estimate the medical insurance costs for three individuals,
# Latoya, Jose, and Wolverine, based on five variables --
# age
# sex: 0 for female, 1 for male
# bmi: body mass index
# num_of_children
# smoker: 0 for a non-smoker, 1 for a smoker

def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
  return estimated_cost

latoya_insurance_cost = calculate_insurance_cost(name = "Latoya", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)

# OUTPUT: The estimated insurance cost for Latoya is 5469.0 dollars.

jose_insurance_cost = calculate_insurance_cost(name = "Jose", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)

# OUTPUT: The estimated insurance cost for Jose is 28336.0 dollars.

wolverine_insurance_cost = calculate_insurance_cost(name = "Wolverine", age = 150, sex = 1, bmi = 53.1, num_of_children = 15, smoker = 1)

# OUTPUT: The estimated insurance cost for Wolverine is 74894.0 dollars.