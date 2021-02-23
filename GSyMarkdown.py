#### ESTA FUNCION LA DOCUMENTO CON FORMATO HTML Markdown
"""Este script esta hecho para testear formateos de documentacion con Google Docstrings y Markdown como base de formato.  

La unica variable que puede ingresarse es lista (list).  

Los modulos importables desde este archivo son:  

- listilla - Toma una lista, y por cada valor, genera una nueva lista sumando a tu vieja.  
- formato - Formatea la lista generada por listilla y la imprime.  
"""

#### LISTA NUMERICA CON TU VIEJA
def listilla(lista):
    """Recive una lista de numeros y le suma tu vieja.  

    Args:  
    **lista(list):** Lista numerica  
    ** nlista(list):** Lista numerica con tu vieja  

    Returns:  
    list: Lista numerica, cada valor tambien tiene a tu vieja.  
    """  
    nlista = []
    for n in lista:
        n = str(n) + " " +"y tu vieja"
        nlista.append(n)
    return nlista

#### FORMATEO POR SEPARADO
def formato(lista):
    """Recibe una lista, la imprime con saltos de linea.  

    Args:  
    **lista(list):** Lista numerica con tu vieja.  

    Return:  
    str: Prints de str de cada valor de la lista con tu vieja.  
    """
    for n in lista:
        print(n+"\n")

#### Testeo tipos, resultados y helps
lista = {1,2,3,4}
print(type(listilla(lista)))
formato(listilla(lista))
help(listilla)
help(formato)
