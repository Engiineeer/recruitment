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
    for index,skill in enumerate(skills,1):
        print(f"{index}. {skill}")


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
     return (
        25 < cv["age"] < 40
        and cv["experience"] > 3
        and desired_skill in cv["skills"]
    )



def main():
    print("Welcome to the special recruitment program, please answer the following questions:" )

    skills = get_skills()
    wanted_skill = 2

    cv = get_user_cv(skills)

    if check_acceptance(cv, skills[wanted_skill]):
        print(f"You have been accepted, {cv['name']}.")
    else:
        print("Sorry, you have been rejected.")


if __name__ == "__main__":
    main()
