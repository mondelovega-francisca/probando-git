import datetime, mensaje1
hoy=datetime.date.today()
prox_cumple=datetime.date(2026,1,10)
diferencia=prox_cumple-hoy
if (hoy==prox_cumple):
    print(mensaje1.mensajeAleat)
else:
    print ('Faltan ', diferencia.days , 'días para mi próximo cumpleaños')   
