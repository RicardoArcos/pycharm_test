from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado
from orden import Orden

teclado1 = Teclado('HP', 'USB')
raton1 = Raton('Razer', 'USB')
monitor1 = Monitor('Asus', 25)
computadora1 = Computadora('Hola', monitor1, teclado1, raton1)

computadoras = [computadora1]
orden1 = Orden(computadoras)
print(orden1)