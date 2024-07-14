import os
import subprocess
import commands as com
import colors 


  
if '__main__' == __name__:
        while True:
            try:   
                user_prompt = input(f"{colors.Colors.GREEN}>>>> {colors.Colors.RESET}")
                parsed=user_prompt.split(' ')
            
                if parsed[0] == '' :
                    print(f"{colors.Colors.RED}Give a non-empty command{colors.Colors.RESET}")
                    continue
                if len(parsed)-1 >= len(com.commands) :
                    print(f"{colors.Colors.CYAN}Give a valid command{colors.Colors.RESET}")
                    continue
                if parsed[0] not in com.commands[len(parsed)-1] :
                    print(f"{colors.Colors.YELLOW}Give a valid command{colors.Colors.RESET}")
                    continue
                
                # len of args not command aka parsed[0]
                length=len(parsed)-1
                command=parsed[0]
                args= parsed[1:] if length>0 else []
                
                # retrieve object from commands list
                args_list= com.commands[length] 
                if command in args_list :
                    args_list[command](args)
                    
            except Exception as e:
                 print(colors.Colors.GREEN + str(e) + colors.Colors.RESET)       
                    

        