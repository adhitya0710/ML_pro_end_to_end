from setuptools import find_packages, setup
from typing import List
hyde='-e .'
def get_requirments(file_path:str)->List[str]:
    requirents=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]
    
    if hyde in requirments:
        requirments.remove(hyde)





setup(
name="ML_PRO_END_TO_END",
version="0.0.1",
author="Adhitya",
author_email="adhitya.gopal0710@gmail.com",
packages=find_packages(),
install_requires=get_requirments('requirments.txt')


)