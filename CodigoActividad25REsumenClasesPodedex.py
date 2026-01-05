#creamos clase Pokemon
class Pokemon:
    def __init__(self,registro,nombre,tipos,descripcion,esta_atrapado):
        self.registro=registro
        self.nombre=nombre
        self.tipos=tipos
        self.descripcion=descripcion
        self.esta_atrapado=esta_atrapado
    #codificamos speak
    def speak(self):
        print(self.nombre+" "+ self.nombre)
    #codificamos display_details
    def display_details(self):
        print("Entry number: "+ str(self.registro))
        print("Nombre: " + str(self.nombre))
        if len(self.tipos)==1:
            print("Tipo: "+ self.tipos[0])
        else:
           print("Tipos: "+ self.tipos[0]+ "y "+ self.tipos[1])
       
        print("Descripcion: "+ self.descripcion)
        if self.esta_atrapado:
            print(self.nombre+" Todavía está atrapado!")
        else:
            print(self.nombre+"  Ya no está atrapado!")    

Bulbasaur1 = Pokemon (1,'Bulbasaur',['Grass','Poison'],'Some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.', False )    
Bulbasaur1.speak()
Bulbasaur1.display_details()
charizard = Pokemon(6, 'Charizard', ['Fire', 'Flying'], 'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.', False)
charizard.speak()
charizard.display_details()
gyarados = Pokemon(130, 'Gyarados', ['Water', 'Flying'], 'It has an extremely aggressive nature. The HYPER BEAM it shoots from its mouth totally incinerates all targets.', False)
gyarados.speak()
gyarados.display_details()
            