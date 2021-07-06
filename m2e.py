#coding:utf-8
import os, django, xlsxwriter

def get_project_name():
    return os.path.split(os.getcwd())[1]
def get_excel_file_name():
    return ''.join([get_project_name(),'.','xlsx'])
def get_settings_module():
    return ''.join([get_project_name(),'.','settings'])
def get_types():
    """
    :return: list
    """
    return None


os.environ.setdefault('DJANGO_SETTINGS_MODULE', get_settings_module())
django.setup()

from django.contrib.contenttypes.models import ContentType
from django.db.models import Empty
def get_model_data(model_type):
    model = model_type.model_class()
    if model is None:
        return None
    model_objects = model_type.get_all_objects_for_this_type()
    if len(model_objects) == 0:
        return None
    model_fields = model._meta.fields
    str_model_fields = list(map(lambda f: f.get_attname(),model_fields))
    all_rows = []
    all_rows.append(str_model_fields)
    for instance in model_objects:
        row = []
        for field in str_model_fields:
            field_value = getattr(instance,field)
            if isinstance(field_value,Empty):
                field_value = ''
            row.append(str(field_value))
        all_rows.append(row)
    return {'col':len(str_model_fields),'data':all_rows}

def main():
    types = get_types()
    if types:
        all_types = list(filter(lambda m: m.name in types, ContentType.objects.all()))
    else:
        all_types = ContentType.objects.all()
    workbook = xlsxwriter.Workbook(get_excel_file_name())
    for model_type in all_types:
        model_data = get_model_data(model_type)
        if model_data is None:
            continue
        sheet = workbook.add_worksheet(model_type.name)
        row_num = 0
        for row in model_data['data']:
            for col in range(model_data['col']):
                sheet.write(row_num,col,row[col])
            row_num += 1
    workbook.close()
if __name__ == '__main__':
    main()






