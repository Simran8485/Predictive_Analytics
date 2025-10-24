from setuptools import find_packages, setup
from typing import List  # Correct capitalization

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements.txt file and returns a list of packages.
    It ignores lines like '-e .' which are editable installs.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newlines and extra spaces
        requirements = [req.strip() for req in requirements]

        # Remove editable installs
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements 

# Setup function
setup(
    name='Predictive_Analytics',
    version='0.0.1',
    author='SIMRAN',
    author_email='12a.simran35507@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.8",
)
