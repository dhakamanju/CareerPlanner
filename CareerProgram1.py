import os

from time import sleep





def skillcheck(skillname):

    loop = True

    boolean = False

    while loop:

        tempInput = input(f'Do you have {skillname}? (Y/N)\n').upper().strip()

        if tempInput == "Y":

            boolean = True

            loop = False

        elif tempInput == "N":

            boolean = False

            loop = False

        else:

            print("Please input either a Y for yes or N for no")    # Error message if invalid



    return boolean



coding = 1          # Default Basic

experience = 1      # Default Beginner

skills = ['Customer Service', 'Patience', 'Communication', 'Attention to Detail', 'Observer', 'Problem Solving',

          'Multitasking', 'Critical Thinking', 'Proactive', 'Growth Mindset', 'Adaptability', 'Teamwork', 'Time Management', 'Persistence', 'Decision Making']      # BSM

certs = ['AZ-900', 'AZ-104', 'AZ-204', 'AZ-400', 'DP-900', 'DP-203', 'AZ-303', 'AZ-304']

career = ['Cloud Support Engineer', 'Quality Assurance Engineer', 'Product Manager', 'DevOps', 'Data Engineer',

          'Software Engineer', 'Cloud Engineer', 'Site Reliability Engineer', 'Cloud Architect']  # career

skillsBool = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]      # default skill value

certsBool = [False, False, False, False, False, False, False, False]      # default skill value

careerValue = [0, 0, 0, 0, 0, 0, 0, 0, 0]                 # career values





os.system('cls')

# Set Coding Skill

loop = True

while loop:

    tempInput = input(f'What is your coding level? (Basic/Intermediate/Expert)?\n').upper().strip()

    if tempInput == "BASIC":

        coding = 1

        loop = False

    elif tempInput == "INTERMEDIATE":

        coding = 2

        loop = False

    elif tempInput == "EXPERT":

        coding = 3

        loop = False

    else:

        print("Please input a valid coding level (Basic/Intermediate/Expert)")    # Error message if invalid



# Set Experience Level

loop = True

while loop:

    tempInput = input(f'What is your experience? (Beginner/Intermediate/High)?\n').upper().strip()

    if tempInput == "BEGINNER":

        experience = 1

        loop = False

    elif tempInput == "INTERMEDIATE":

        experience = 2

        loop = False

    elif tempInput == "HIGH":

        experience = 3

        loop = False

    else:

        print("Please input a valid experience level (Beginner/Intermediate/High)")    # Error message if invalid



index = 0

for i in certs:

    certsBool[index] = skillcheck(certs[index])   # Run function for each certificate

    index += 1



index = 0

for i in skills:

    skillsBool[index] = skillcheck(skills[index])   # Run function for each skill

    index += 1

os.system('cls')



# Career logic ===

if skillsBool[0]:           # Customer Service

    careerValue[0] += 1     # Cloud Support Engineer    +1

    careerValue[8] += 1     # Cloud Architect           +1

if skillsBool[1]:           # Patience

    careerValue[0] += 1     # Cloud Support Engineer    +1

if skillsBool[2]:           # Communication

    careerValue[0] += 1     # Cloud Support Engineer    +1

    careerValue[3] += 1     # DevOps                    +1

    careerValue[8] += 1     # Cloud Architect           +1

if skillsBool[3]:           # Attention to Detail

    careerValue[1] += 1     # Quality Assurance Engineer+1

    careerValue[2] += 1     # Product Manager           +1

    careerValue[4] += 1     # Data Engineer             +1

    careerValue[5] += 1     # Software Engineer         +1

if skillsBool[4]:           # Observer

    careerValue[1] += 1     # Quality Assurance Engineer+1

    careerValue[2] += 1     # Product Manager           +1

if skillsBool[5]:           # Problem Solving

    careerValue[1] += 1     # Quality Assurance Engineer+1

    careerValue[2] += 1     # Product Manager           +1

    careerValue[4] += 1     # Data Engineer             +1

    careerValue[5] += 1     # Software Engineer         +1

if skillsBool[6]:           # Multitasking

    careerValue[3] += 1     # DevOps                    +1

    careerValue[4] += 1     # Data Engineer             +1

    careerValue[7] += 1     # Site Reliability Manager  +1

if skillsBool[7]:           # Critical Thinking

    careerValue[3] += 1     # DevOps                    +1

    careerValue[5] += 1     # Software Engineer         +1

if skillsBool[8]:           # Proactive

    careerValue[3] += 1     # DevOps                    +1

    careerValue[6] += 1     # Cloud Engineer            +1

if skillsBool[9]:           # Growth Mindset

    careerValue[6] += 1     # Cloud Engineer            +1

if skillsBool[10]:          # Adaptability

    careerValue[6] += 1     # Cloud Engineer            +1

if skillsBool[11]:          # Teamwork

    careerValue[6] += 1     # Cloud Engineer            +1

if skillsBool[12]:          # Time Management

    careerValue[7] += 1     # Site Reliability Manager  +1

if skillsBool[13]:          # Persistence

    careerValue[7] += 1     # Site Reliability Manager  +1

if skillsBool[14]:          # Decision Making

    careerValue[8] += 1     # Cloud Architect           +1



# Display logic ===

# 3 for most

# 4 for careerValue[6] && careerValue[3]

index2 = 10 # Max points

found = False

while index2 > 3:   # Minimum points to list

    index2 -= 1

    index = 0

    for i in career:



        if careerValue[index] == index2:

            #print(f'{career[index]} value = {careerValue[index]}\n') #Debug code (remove # to check values)



            if index == 0:                                                  # Cloud Support Engineer Check

                if certsBool[0] and certsBool[1]:

                    if coding >= 1 and experience >= 1:

                        print(f'{career[index]} is the career for you!\n')

                        # do career action (display info here)

                        found = True

            if index == 1:                                                  # Quality Assurance Engineer Check

                if certsBool[0]:

                    if coding >= 1 and experience >=1:

                        print(f'{career[index]} is the career for you!\n')

                        # do career action (display info here)

                        found = True

            if index == 2:                                                  # Product Manager Check

                if certsBool[0]:

                    if coding >= 1 and experience >= 2:

                        print(f'{career[index]} is the career for you!\n')

                        # do career action (display info here)

                        found = True

            if index == 3:                                                  # DevOps Check

                if certsBool[0] and certsBool[1] and certsBool[2] and certsBool[3]:

                    if coding >= 3 and experience >= 2:

                        print(f'{career[index]} is the career for you!\n')

                        # do career action (display info here)

                        found = True

            if index == 4:                                                  # Data Engineer Check

                if certsBool[0] and certsBool[4] and certsBool[5]:

                    if coding >= 3 and experience >= 2:

                        print(f'{career[index]} is the career for you!\n')

                        # do career action (display info here)

                        found = True

            if index == 5:                                                  # Software Engineer Check

                if certsBool[0] and certsBool[2] and certsBool[6]:

                    if coding >= 3 and experience >= 2:

                        print(f'{career[index]} is the career for you!\n')

                        # do career action (display info here)

                        found = True

            if index == 6:                                                  # Cloud Engineer Check

                if certsBool[0] and certsBool[1]:

                    if coding >= 3 and experience >= 2:

                        print(f'{career[index]} is the career for you!\n')

                        # do career action (display info here)

                        found = True

            if index == 7:                                                  # Site Reliability Engineer Check

                if certsBool[0]:

                    if coding >= 3 and experience >= 2:

                        print(f'{career[index]} is the career for you!\n')

                        # do career action (display info here)

                        found = True

            if index == 8:                                                  # Cloud Architect Check

                if certsBool[0] and certsBool[6] and certsBool[7]:

                    if coding >= 2 and experience >= 3:

                        print(f'{career[index]} is the career for you!\n')

                        # do career action (display info here)

                        found = True

        index += 1

if found == False:

    print('You are not a good fit for a cloud job with your current qualifications and skill set') # If no conditions are met

sleep(30006) # This just stops it from closing straight away so you can read the results
