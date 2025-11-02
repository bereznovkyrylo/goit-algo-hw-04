import sys
from pathlib import Path
from colorama import Fore,Style


def main(direction,level=0):

    try:    
        path=Path(direction)
        spaces='    '*level

        for item in path.iterdir():
            if item.is_dir():
                print(spaces,Fore.BLUE + item.name +'/',Style.RESET_ALL)
                if not 'env' in item.name : # skip venv/.env/env/.venv folders 

                    main(item,level+1)
                continue
            else:
                 print(spaces,Fore.YELLOW + item.name,Style.RESET_ALL)

            
    except Exception as e:
        print(Fore.RED + f'{e}' ,Style.RESET_ALL)



if __name__=='__main__':
    if len(sys.argv) !=2:
        print(f'{Fore.RED + '[error]'} Wrong path to file',Style.RESET_ALL)
    else:
        main(sys.argv[1])

            


