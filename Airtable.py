from airtable import Airtable  #python has in-build lib to work on airtable

try:
    base_key = 'appT41cyXCI2uF9dM'  # Base ID of working base
    table_name = 'Data_pattern'  # name of the table in your working base
    api_key = 'keykdQiIrNHHt3az8'  # API Key
except Exception:
    print("Authentication Error")

airtable = Airtable(base_key, table_name, api_key)
pages = airtable.get_iter(maxRecords=2)
empty_list=[]
for page in pages:
    for record in page:
        data=record      #written data in JSON format
        for i,j in data.items():
            if i=="fields":
                Final_data=j
        for item in Final_data.values():
            empty_list.append(item)
employee=empty_list      #['working on zoho corp. completed his work', 'John', 'Done', 'working as Dev in Awn org.Working on pending task', 'Ben', 'In progress']
employee1=empty_list[:3] #['working on zoho corp. completed his work', 'John', 'Done']
employee2=empty_list[3:] #['working as Dev in Awn org.Working on pending task', 'Ben', 'In progress']




