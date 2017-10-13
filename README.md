# Django-Model-to-Excel
A simple tool for converting django models to excel file without polluting you application.

## Quick Start
Just smiply download the `m2e.py` script and put it under the root of your django project where your `manage.py` locates and run `python m2e.py`, an excel file will be generated.

## Config
By default, name of generated excel file wil be `your_project_name.xlsx` and all available models will be converted.
For changing the config, you can open the script and rewrite `get_excel_file_name` fcuntion for changing the generated filename. Also, you can rewrite `get_types` function which should return a list of model names. 

## Dependency
1. `django` >= 1.8 
2. `python` >= 2.7 or 3.3
3. `xlsxwriter` >= 0.9.3
