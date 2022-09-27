# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from


import re


def get_skills():
    skills=["Python","C++","Javascript"]
    return skills


# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    print("Skills: ")
    for skill in skills:
        print(f"1. {skill}")


# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    show_skills(skills)
    input_skill_1 = int(input("\nChoose a skill from above by entering its number: "))
    input_skill_2 = int(input("Choose another skill from above by entering its number: "))
    user_skill=[]
    if input_skill_1 == 1:
        user_skill.append(skills[0])
    elif input_skill_1 == 2:
        user_skill.append(skills[1])
    elif input_skill_1 == 3:
        user_skill.append(skills[2])

    if input_skill_2 == 1:
        user_skill.append(skills[0])
    elif input_skill_2 == 2:
        user_skill.append(skills[1])
    elif input_skill_2 == 3:
        user_skill.append(skills[2])
    return user_skill



# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    name= input("What's your name? ")
    age = input("How old are you? ")
    experience = input("How many years of experience do you have? ")
    cv={
        "name":name,
        "age":age,
        "experience":experience,
        "skills":get_user_skills(skills)
    }
    return cv



# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if cv in desired_skill:
        return True
    else:
        return False



def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    
    print(get_user_cv(get_skills()))


if __name__ == "__main__":
    main()
