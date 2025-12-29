#Create a dictionary named student_scores where the key is a student's name and the value is a list of three exam marks.
#Action: Calculate the average for one student.
#Goal: Print True if their average is greater than or equal to 60, and False otherwise.

student_scores = {'bishwas': [70, 65, 60]}
score = student_scores['bishwas']
average = sum(score) / len(score)
print(average >= 60)


# Topic: Membership & Logical Operators
# Create a dictionary named stock with items and their quantities:stock = {"apples": 10, "bananas": 2, "oranges": 0}
# Action: Check if "pears" is in the dictionary using the in operator.
# Action: Use a logical operator to check if "bananas" are in stock and if the quantity is less than 5.
# Goal: If both are true, print "Time to restock bananas!".


# Start with a dictionary: users = {"admin": "1234"}
# Step 1: Add a new user to the dictionary using assignment (users["teacher"] = "password789").
# Step 2: Create two variables, input_user and input_pass.
# Step 3: Use == and and to check if the input_user exists as a key and if the input_pass matches the value.
# Goal: Print "Access Granted" if they match.
users = {"admin": "1234"}
users["teacher"] = "password789" # step 1 key value inserting . (like user= teacher)
input_user = "teacher"
input_pass = "password789" #step 2
if input_user in users and users[input_user] == input_pass: # step 3
    print("Access Granted")
else: 
    print("Access Denied")
