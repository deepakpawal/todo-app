file_name=input("Enter today's date")

mood=input("Hpw dp you rate your mood today from 1 to 10?")

journal= input("Let you thoughts flow:")

with open(f"{file_name}.txt",'w') as file:
    file.writelines(journal)