import pandas as pd
# from .models import Usuario
from usuario.models import Usuario
# import usuario.Usuario


tmp_data=pd.read_csv('file.csv',sep=';')
#ensure fields are named~ID,Product_ID,Name,Ratio,Description
#concatenate name and Product_id to make a new field a la Dr.Dee's answer
usuarios = [
    Usuario(
        drt = tmp_data.ix[row]['drt'],
        nome = tmp_data.ix[row]['nome'],
        cargo = tmp_data.ix[row]['cargo'],
        perfil_acesso = tmp_data.ix[row]['perfil'],

        # description = tmp_data.ix[row]['Description'],
        # price = tmp_data.ix[row]['price'],
    )
    for row in tmp_data['ID']
]
Usuario.objects.bulk_create(usuarios)
