from setuptools import find_packages, setup
from typing import List
Hyphen_dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if Hyphen_dot in requirements:
            requirements.remove(Hyphen_dot)

    return requirements



setup(
name = "ML project",
version = "0.0.1",
author='Anas',
author_email='anaspp944@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)