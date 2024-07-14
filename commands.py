import os
import colors
def list_directories(args):
    """
    Returns a list of all the files and directories in the current working directory.
    :param args(list): A list of arguments passed to the function. This parameter is not used in the function and can be ignored.
    :prints: A list of strings representing the names of the files and directories in the current working directory.
    """
    print(colors.Colors.BLUE + str(os.listdir(os.getcwd())) + colors.Colors.RESET)
    
def current_working_directory(args):
    """
    Retrieves the current working directory.
    Args: args(list): The command line arguments passed to the function.
    prints str: The current working directory.
    """
    print(colors.Colors.YELLOW + os.getcwd() + colors.Colors.RESET)

def clear(args):
    """
    A function that clears the console screen based on the operating system.
    Args: args(list): The command line arguments passed to the function.
    Returns:  None
    """
    os.system('clear' if os.name == 'posix' else 'cls')



commands=[
{
    'ls': list_directories,
    'cwd': current_working_directory,
    'clr': clear
},
          
]