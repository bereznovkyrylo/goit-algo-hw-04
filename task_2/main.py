from pathlib import Path
current_dir=Path(__file__).parent

def get_cats_info(path_to_file):
    all_cats=[]
    try:
        with open(path_to_file,'r',encoding='utf-8') as file:
            for cat in file.readlines():

                (id,name,year)=cat.split(',')
                all_cats.append({"id":id,"name":name,'year':float(year)})

        return all_cats
    
    except FileNotFoundError:
        print('Wrong path')
    except OSError:
        print('OSError')

if __name__=='__main__':
    print(get_cats_info(current_dir/"cats.txt"))