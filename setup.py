from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirements_list:List[str]= []

    try:
        # Open and read the requirement.txt file
        with open('requirements.txt','r') as file:
            # read lines from the file
            lines = file.readlines()
            # process each line
            for line in lines:
                # Strip whitespace and newline characters
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_list
print(get_requirements())

setup(
    name ="AI-TRAVEL-PLANNER",
    version= "0.0.1",
    author="hasnain",
    author_email="hasnainchanna172@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)