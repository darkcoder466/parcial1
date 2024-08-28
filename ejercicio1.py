class Lapicero:
    def __init__(self,marca,color,precio):
        self.marca=marca
        self.color=color
        self.precio=precio
    
    
LapiceroRojo = Lapicero("sharpi","rojo",3000)
LapiceroNegro = Lapicero("paper mate", "negro",2000)

print(f"el lapicero es de color {LapiceroRojo.color}, de marca {LapiceroRojo.marca}, su precio es de {LapiceroRojo.precio}$ y es del tipo {type(LapiceroRojo)}")

print(f"el lapicero es de color {LapiceroNegro.color}, de marca {LapiceroNegro.marca}, su precio es de {LapiceroNegro.precio}$ y es del tipo {type(LapiceroNegro)}")





