from datetime import datetime

"""Este script esta hecho para testear formateos de documentacion con reStructured como base de formato.

La unica variable que puede ingresarse es mensaje (str).

Los modulos importables desde este archivo son:

    * hora - Te devuelve el mensaje que pasaste y le agrega la hora de datetime.now()
"""
#ESTA FUNCION LA DOCUMENTO CON FORMATO reStructured
def hora(mensaje):
    """Recive un mensaje y retorna el mensaje mas la hora actual en la que se llamo la funcion.

    :param mensaje: Mensaje a retornar
    :type mensaje: str
    :param ahora: Llamada a datetime.now()
    :type ahora: str
    :returns: string con mensaje + un espacio + la hora actual con el formato de datetime.now()
    :rtype: str
    """
    ahora = datetime.now()
    return mensaje + " " + str(ahora)

#Testeo tipos, resultados y helps
test = (hora("Jaja nos vimos"))
print(test)
print(type(test))

help(hora)