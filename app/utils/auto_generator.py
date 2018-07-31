import pandas as pd
from jinja2 import Environment, Template,FileSystemLoader
import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


csv_paths  = ["D:/survey.csv", "D:/billing.csv"]
template_path = "D:/templates"
model_names = ['Survey','Billing']
model_files= ['survey.py','billing.py']


def main():
    real_file_paths = []
    for file in model_files:
        real_file_paths.append(dir_path +'\\' +file)

    for count, item in enumerate(model_files):
        with open(real_file_paths[count], 'w') as f:
            print(real_file_paths[count])
            print(auto_genearte_from_csv_to_model(csv_paths[count], template_path[count],model_names[count]))
            f.write(auto_genearte_from_csv_to_model(csv_paths[count], template_path[count],model_names[count]))



def auto_genearte_from_csv_to_model(csv_path, tempalte_path, model_name):
    if not csv_path and tempalte_path and model_name:
        return "parameters error"
    
    loader = FileSystemLoader(template_path)
    env = Environment(
        loader=loader
    )

    headers = pd.read_csv(csv_path, nrows=1, encoding ='latin1').columns.tolist()
    raw_headers = []
    for head in headers:
        if '(' in head:
            f_head = re.sub(r'\([^()]*\)', '', head)
            raw_headers.append(f_head)

        elif ':' in head:
            f_head = head.replace(":", "")
            raw_headers.append(f_head)
        elif '-' in head:
            f_head = head.replace('-', "")
            raw_headers.append(f_head)
        else:
            raw_headers.append(head)

    clean_headers = []       
    for head in raw_headers:
        head = re.sub( '\s+', ' ', head ).strip()
        clean_headers.append(head.replace(" ", "_").lower())
    template = env.get_template('test.py')

    return template.render(navigation = clean_headers, class_name = model_name)

if __name__ =="__main__":
    main()