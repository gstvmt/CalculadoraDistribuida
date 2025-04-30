# saved as greeting-client.py
import Pyro5.api

ns = Pyro5.api.locate_ns(host="192.168.1.4", port=9090)
uri = ns.lookup("calculadora")
calc = Pyro5.api.Proxy(uri)

print("5 + 3 =", calc.soma(5, 3))
print("10 - 4 =", calc.subtrai(10, 4))
print("7 * 6 =", calc.multiplica(7, 6))
print("8 / 2 =", calc.divide(8, 2))
print("4**(1/2) =", calc.raiz(4))
print("4**2 =", calc.potencia(4, 2))
