from pathlib import Path
current_dir=Path(__file__).parent

def total_salary(path_to_file):
    try:
        with open(path_to_file,'r',encoding='utf-8') as file:

            all_salaries=[float(x.split(',')[1]) for x in file.readlines()]
            total=sum(all_salaries)

            return (total,total/len(all_salaries))
    except Exception as e:
        print(f'{e} with file')
    



if __name__=='__main__':
    total, average = total_salary(current_dir/"salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")