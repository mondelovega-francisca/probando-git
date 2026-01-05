class City:
 def __init__(self, nombre,pais,poblacion,alcalde,fundacion,landmark):
  self.nombre=nombre
  self.pais=pais
  self.poblacion=poblacion
  self.alcalde=alcalde
  self.fundacion=fundacion
  self.landmark=landmark

Ourense=City('Ourense','España',105000,'Gonzalo Pérez Jácome',1122,['Pontevedra','Lugo','Portugal','Castilla y Leon'])
Sidney=City('Sidney','Australia',5297000,'Clover Moore',1788,['Océano Pacífico', 'río Hawkersbury', 'Parque Nacional Real','Montañas Azules'] )

print(vars(Ourense))
print(vars(Sidney))
