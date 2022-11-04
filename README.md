# DATATHON-PI02

El objetivo de este Datathon era predecir si una propiedad de Colombia era barata o cara.

EL dataset utilizado tenía gran cantidad de nulos en campos importantes como la latitud, la longitud y la superficie entonces, se decidió predecir si una propiedad es cara o no analizando con lenguaje natural la descripción de cada propiedad, específicamente se usó TF-TDI.

La variable objetivo fue calculada en función al promedio del precio. Si el precio de una propiedad era igual o superior al promedio, esta era considerada cara, de lo contrario era considerada barata.

Por último, para realizar la predicción se utilizó Random Forest. 
