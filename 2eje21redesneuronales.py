import numpy as np
#capa de numeros que dice cuánto importa cada dato de entrada para cada neurona de la primera capa oculta
w0 = np.array([[ 1.19627687e+01,  2.60163283e-01],
               [ 4.48832507e-01,  4.00666119e-01],
                   [-2.75768443e-01,  3.43724167e-01],
                   [ 2.29138536e+01,  3.91783025e-01],
                   [-1.22397711e-02, -1.03029800e+00]])
#Capa oculta 1 con dos nodos. Convierte los dos valores de la capa primera en 2 valores nuevos
w1 = np.array([[11.5631751 , 11.87043684],
                   [-0.85735419,  0.27114237]])
#Capa oculta 2 con dos nodos. Convierte los dos valores de la segunda capa en un único número. el precio
w2 = np.array([[11.04122165],
                   [10.44637262]])
#coeficientes para calcular el precio b2 termino independiente
b0 = np.array([-4.21310294, -0.52664488])
b1 = np.array([-4.84067881, -4.53335139])
b2 = np.array([-7.52942418])

x = np.array([[111, 13, 12, 1, 161],
                 [125, 13, 66, 1, 468],
                 [46, 6, 127, 2, 961],
                 [80, 9, 80, 2, 816],
                 [33, 10, 18, 2, 297],
                 [85, 9, 111, 3, 601],
                 [24, 10, 105, 2, 1072],
                 [31, 4, 66, 1, 417],
                 [56, 3, 60, 1, 36],
                 [49, 3, 147, 2, 179]])
y = np.array([335800., 379100., 118950., 247200., 107950., 266550.,  75850.,
                93300., 170650., 149000.])


def hidden_activation(z):
    # ReLU activation. fix this!
    # Compara 0 con z y se queda con el mayor
    return np.maximum(0, z)

def output_activation(z):
    # identity (linear) activation. fix this!
    return z

x_test = [[82, 2, 65, 3, 516]]
for item in x_test:
    h1_in = np.dot(item, w0) + b0 # this calculates the linear combination of inputs and weights
    h1_out = hidden_activation(h1_in) # apply activation function
    #h1_in va a dar un vector de dos números. se multiplica wo *xtest
    #neurona_1 
#82*11.96 +
#2*0.44 +
#65*(-0.27) +
#3*22.91 +
#516*(-0.01)

#neurona_2 =
#82*0.26 +
#2*0.40 +
#65*0.34 +
#3*0.39 +
#516*(-1.03)

    # second hidden layer
    h2_in = np.dot(h1_out, w1) + b1
    h2_out = hidden_activation(h2_in)
    
    # output layer
    out_in = np.dot(h2_out, w2) + b2
    out = output_activation(out_in)
    
    print(out[0])