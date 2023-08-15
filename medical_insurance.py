# These are the initial variables I will consider when estimating 
# medical insurance costs

age = 28
sex = 0 # 0 for female, 1 for male
bmi = 26.2
num_of_children = 3
smoker = 0 # 0 for a non-smoker, 1 for a smoker

# After the declaration of the variables, the variable below, 
# 'insurance_cost', will utilize the following insurance estimate formula

insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print(insurance_cost)

# OUTPUT: 5469.0
# Displayed informatively --

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# OUTPUT: This person's insurance cost is 5469.0 dollars.

# Using the plus-equal operator, I will add 4 years to the age variable
# Remember: The starting age was 28!

age += 4
print(age)

# OUTPUT: 32
# Now that the age has changed, I have to recalculate the insurance cost
# by declaring a new variable called new_insurance_cost.

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print(new_insurance_cost)

# OUTPUT: 6469.0
# Next, I will find the difference between the new_insurance_cost 
# and the previous insurance_cost.
# So a new variable called, change_in_insurance_cost is set equal 
# to the difference.

change_in_insurance_cost = new_insurance_cost - insurance_cost

# Then I can say --

print("People who are four years older have estimated insurance costs that are " + str(change_in_insurance_cost) + " dollars different.")

# OUTPUT: People who are four years older have estimated insurance costs that are 1000.0 dollars different.
# I will display this information in an informative way --

print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

# OUTPUT: The change in cost of insurance after increasing the age by 4 years is 1000.0 dollars.

# Now, I will be resetting the value of age back to 28 and adding 3.1 to the bmi.

age = 28
bmi += 3.1
print(age)
print(bmi)

# OUTPUT: age = 28, bmi = 29.3
# Now that the BMI has changed by 3.1 points, let's find out how that change 
# affects insurance costs!
# New variable name, new_insurance_cost, attached to insurance cost formula --

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print(new_insurance_cost)

# OUTPUT: 6616.0
# Saving the difference between new_insurance_cost and insurance_cost 
# in a variable called change_in_insurance_cost --

change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in the estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")

# OUTPUT: The change in the estimated insurance cost after increasing BMI by 3.1 is 1147.0 dollars.

# Let's look at the effect sex has on medical insurance costs.
# I will reassign the bmi variable back to its original value of 26.2.
# The value of sex is reassigned to 1, because 1 identifies a male individual
# and 0 identifies a female individual.

bmi -= 3.1
sex = 1
print(bmi)

# OUTPUT: bmi = 26.2
# The rewritten insurance cost formula --

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print(new_insurance_cost)

# OUTPUT: 5341.0
# And now the difference --

change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in the estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")

# OUTPUT: The change in the estimated cost for being male instead of female is -128.0 dollars.
# Notice that this time we got a negative value for change_in_insurance_cost!
# We changed the sex variable from 0 (female) to 1 (male) and it decreased the estimated insurance costs.
# This means that men tend to have lower medical costs on average than women.

# NEXT!!
# We'll create another bunch of variables below for a 
# 42-year-old, smoking woman who has 5 children and a BMI of 32.5.

age += 14
sex = 0
bmi += 6.3
num_of_children = 5
smoker = 1
print(age)
print(bmi)

# OUTPUT: age = 42, bmi = 32.5
# The rewritten insurance cost formula --

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print(new_insurance_cost)

# OUTPUT: 36150.0
# And now the difference --

change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for a 42-yr-old female with a BMI of 32.5, 5 children, and smokes is " + str(change_in_insurance_cost) + " dollars.")

# OUTPUT: The change in estimated cost for a 42-yr-old female 
# with a BMI of 32.5, 5 children, and smokes is 30681.0 dollars.