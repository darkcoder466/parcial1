
class Ropa:
    def __init__(self,marca,color,tipo):
        self.marca=marca
        self.color=color
        self.tipo=tipo
    
    
camisa = Ropa("gucci","rojo","prenda superior")
guantes= Ropa("columbia", "negro","accesorio")

print(f"la camisa es de color {camisa.color}, de marca {camisa.marca} y es del tipo {camisa.tipo}")


print(f"los guantes son de color {guantes.color}, de marca {guantes.marca} y es del tipo {guantes.tipo}")
