# sierto el numero de nombres q entras tiene q ser par, no le puse proteccion contra eso

class Sorteo(object):
    def __init__(self):
        """
        Inicializacion de variables e importacion del numero aleatorio
        """
        from random import randint as rand
        self.rand = rand
        self.count=0
        self.lista=[]
        self.deny_list=[]
        self.fd_w= open("sorteo", "w")
        self.fd_r= open("sorteo", "r")

    def obtener_lista(self):
        """
        obtener la lista por medio del teclado
        nota: puede obtenerse de cualquier lugar
        """
        while True:
            entrada=input("Ingrese un Nombre: ")
            if entrada == "":
                break

            if not entrada in self.lista:
                self.lista.append(entrada)
        self.deny_list=self.lista

    def dice(self):
        """
        obtener 2 numeros aleatorios
        """
        while True:
            self.num1 = self.rand(0,len(self.deny_list)-1)
            self.num2 = self.rand(0,len(self.deny_list)-1)
            if self.num1 != self.num2:
                break
        return [self.num1,self.num2]

    def proccess(self):
        while True:
            num1,num2 = self.dice()
            subject_1 = self.deny_list[num1]
            subject_2 = self.deny_list[num2]
            self.deny_list.remove(subject_1)
            self.deny_list.remove(subject_2)
            print (f"{subject_1} <-> {subject_2}")
            if len(self.deny_list) == 0:
                break
                

if __name__ == "__main__":
    var = Sorteo()
    var.obtener_lista()
    var.proccess()
