class Vehiculo:
    def __init__(self,tipo,modelo,tipoDeMotor,capacidadDeCarga):
        self.tipo = tipo
        self.modelo = modelo
        self.tipoDeMotor = tipoDeMotor
        self.capacidadDeCarga = capacidadDeCarga
    
    
avion = Vehiculo("aereo","Boeing 737","combustion",8500)
motocicleta = Vehiculo("terrestre", "yamaha","electrico",300)
yate = Vehiculo("acuatico","Azimut 60 Flybridge","combustion",3500)


print(f"el avion es del tipo '{avion.tipo}', su modelo es '{avion.modelo}',su motor es a '{avion.tipoDeMotor}' y tiene una capcidad de carga de '{avion.capacidadDeCarga} kilos'")

print(f"la moticicleta es del tipo '{motocicleta.tipo}', su modelo es '{motocicleta.modelo}',su motor es '{motocicleta.tipoDeMotor}' y tiene una capacidad de carga de '{motocicleta.capacidadDeCarga} kilos'")

print(f"el yate es del tipo '{yate.tipo}', su modelo es '{yate.modelo}',su motor es '{yate.tipoDeMotor}' y tiene una capacidad de carga de '{yate.capacidadDeCarga} kilos'")

