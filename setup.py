from setuptools import find_packages,setup

setup(
    name = "mcqgenretor",
    version="0.0.1",
    author='omkar gaikwad',
    author_email="omigaikwad.og@gmail.com",
    install_requres = ["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)