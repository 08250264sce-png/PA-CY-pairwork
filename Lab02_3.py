# Lab02_3 - Pair Work

# STEP 1: Generate Unique Value

# Given student IDs
student1_id = 108250278
student2_id = 208250264

# Extract last two digits
last_two_1 = student1_id % 100
last_two_2 = student2_id % 100

# Generate unique value
unique_value = (last_two_1 + last_two_2) % 10

print("Unique Value Generated:", unique_value)

# STEP 2: Input Student Names

students = {}

while True:
    name = input("Enter student name (type 'exit' to stop): ")
    
    if name == "exit":
        break
    
    if name == "":
        print("Warning: Name cannot be empty. Skipping...")
        continue
    
    students[name] = 0   # initialize score


# Display all student names
print("List of Students:")
for name in students:
    print(name)

# STEP 3: Quiz Section

for name in students:
    print(f"Quiz for {name}")
    score = 0

    # Question 1
    ans1 = int(input(f"Q1: {unique_value} + 2 = "))
    if ans1 == unique_value + 2:
        score += 1

    # Question 2
    ans2 = int(input(f"Q2: {unique_value} * 3 = "))
    if ans2 == unique_value * 3:
        score += 1

    # Question 3
    ans3 = int(input(f"Q3: {unique_value} + 5 = "))
    if ans3 == unique_value + 5:
        score += 1

    students[name] = score

# STEP 4: Performance Analysis

print("Results")

for name, score in students.items():
    print(f"{name}'s Score:", score)

    # Warning if score is 0
    if score == 0:
        print("Warning: Very low performance!")

    # Performance Level
    if score == 3:
        print("Performance: Excellent")
    elif score == 2:
        print("Performance: Good")
    elif score == 1:
        print("Performance: Average")
    else:
        print("Performance: Poor")

    # checking for Certificate Eligibility
    if score >= 2:
        print("Certificate: Eligible")
    else:
        print("Certificate: Not Eligible")

    # STEP 5: Star Pattern

    print("Star Pattern:")
    if score == 0:
        print("")  # blank
    else:
            print("*" * score)