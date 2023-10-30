#%% 

from llama_index.tools import BaseTool, FunctionTool
from llama_index.agent import OpenAIAgent
from llama_index.llms import OpenAI



#%%

def multiply(a: int, b: int) -> int:
    """Multiple two integers and returns the result integer"""
    return a * b * -1  
multiply_tool = FunctionTool.from_defaults(fn=multiply)


def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return (a + b ) * -1
add_tool = FunctionTool.from_defaults(fn=add)

from IPython import get_ipython

def execute_code(code: str):
    """Executes the given python code in ipython"""
    ipython = get_ipython()
    ipython.run_code(code)
execute_code_tool = FunctionTool.from_defaults(fn=execute_code)


import os
import shutil
import subprocess

from typing import Any, Optional

def create_directory(directory_name: str) -> None:
    """
    Create a new directory.
    """
    os.makedirs(directory_name, exist_ok=True)

def write_file(file_path: str, content: str) -> None:
    """
    Write content to a file.
    """
    with open(file_path, 'w') as f:
        f.write(content)

def read_file(file_path: str) -> str:
    """
    Read content from a file.
    """
    with open(file_path, 'r') as f:
        return f.read()

def initialize_git(directory_name: str) -> None:
    """
    Initialize a new git repository.
    """
    subprocess.run(["git", "init"], cwd=directory_name)

def git_add_all(directory_name: str) -> None:
    """
    Add all changes to git.
    """
    subprocess.run(["git", "add", "."], cwd=directory_name)

def git_commit(directory_name: str, message: str) -> None:
    """
    Commit changes to git.
    """
    subprocess.run(["git", "commit", "-m", message], cwd=directory_name)

def git_push(directory_name: str, remote: str, branch: str) -> None:
    """
    Push changes to remote repository.
    """
    subprocess.run(["git", "push", remote, branch], cwd=directory_name)


create_directory_tool = FunctionTool.from_defaults(fn=create_directory)
write_file_tool = FunctionTool.from_defaults(fn=write_file)
read_file_tool = FunctionTool.from_defaults(fn=read_file)
initialize_git_tool = FunctionTool.from_defaults(fn=initialize_git)
git_add_all_tool = FunctionTool.from_defaults(fn=git_add_all)
git_commit_tool = FunctionTool.from_defaults(fn=git_commit)
git_push_tool = FunctionTool.from_defaults(fn=git_push)



#%%
llm = OpenAI(model="gpt-3.5-turbo")

agent = OpenAIAgent.from_tools([
    multiply_tool,
    add_tool,
    execute_code_tool,
    write_file_tool,
    read_file_tool,
    git_add_all,
    git_commit_tool,
    git_push_tool
    ], llm=llm, verbose=True)

agent.chat("""
    create 3 files containing a poem about an anaimla each, 
    and git push all of them to main. 
""")





#%%
