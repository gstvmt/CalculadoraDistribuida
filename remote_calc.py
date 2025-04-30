import Pyro5.api
import math

@Pyro5.api.expose
class Calculadora_Remota(object):
    def soma(self, a, b):
        return a + b
    def subtrai(self, a, b):
        return a - b
    def multiplica(self, a, b):
        return a*b
    def divide(self, a, b):
        return a/b
    def raiz(self, a):
        return math.sqrt(a)
    def potencia(self, b, e):
        return math.pow(b, e)

daemon = Pyro5.server.Daemon()         # make a Pyro daemon
ns = Pyro5.api.locate_ns()             # find the name server
uri = daemon.register(Calculadora_Remota)   # register the greeting maker as a Pyro object
ns.register("calculadora", uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls
