import math
           
def calculo_con_base_y_altura(base, altura):
    base = float(base)
    altura = float(altura)
    area = altura*base/2
    area = round(area, 2)
    area = str(area)
    
    return area
   
def calculo_con_tres_lados(lado_a, lado_b, lado_c):
    lado_a = float(lado_a)
    lado_b = float(lado_b)    
    lado_c = float(lado_c)
    area = 0.25 * math.sqrt((lado_a**2 + lado_b**2 + lado_c**2)**2 - 2*(lado_a**4 + lado_b**4 + lado_c**4))
    area = round(area, 2)
    area = str(area)

    return area
               
def calculo_con_dos_lados_un_angulo(lado_a, lado_b, angulo_x):    
    lado_a = float(lado_a)
    lado_b = float(lado_b)
    angulo_x = float(angulo_x)
    angulo_x = angulo_x*math.pi/180
    area = lado_a*lado_b*math.sin(angulo_x)/2
    area = round(area, 2)
    area = str(area)

    return area

def calculo_de_lado_c_faltante(lado_a, lado_b, angulo_x):
    lado_a = float(lado_a)
    lado_b = float(lado_b)
    angulo_x = float(angulo_x)
    angulo_x = angulo_x*math.pi/180
    lado_c = math.sqrt((lado_a**2) + (lado_b**2) - (2*lado_a*lado_b * (math.cos(angulo_x))))
    lado_c = round(lado_c, 0)

    return lado_c

def calculo_con_un_lado_dos_angulos(lado_a, angulo_x, angulo_y):
    lado_a = float(lado_a)
    angulo_x = float(angulo_x)
    angulo_x = angulo_x * math.pi / 180
    angulo_y = float(angulo_y)
    angulo_y = angulo_y * math.pi / 180
    area = (lado_a ** 2 * (math.sin(angulo_y)) * (math.sin(angulo_x))) / (2 * math.sin(angulo_y + angulo_x))
    area = round(area, 2)
    area = str(area)

    return area

def calculo_del_lado_b_faltante(lado_a, angulo_x, angulo_y):
    lado_a = float(lado_a)
    angulo_x = float (angulo_x)
    angulo_x = angulo_x*math.pi/180
    angulo_y = float (angulo_y)
    angulo_y = angulo_y*math.pi/180
    angulo_z = math.pi -(angulo_y + angulo_x)
    lado_b = (lado_a*math.sin(angulo_y))/math.sin(angulo_z)
    lado_b = round(lado_b, 2)

    return lado_b

def calculo_del_lado_cc_faltante(lado_a, angulo_x, angulo_y):
    lado_a = float(lado_a)
    angulo_x = float(angulo_x)
    angulo_x = angulo_x * math.pi / 180
    angulo_y = float(angulo_y)
    angulo_y = angulo_y * math.pi / 180
    angulo_z = math.pi - angulo_y - angulo_x
    lado_c = lado_a * math.sin(angulo_x) / math.sin(angulo_z)
    lado_c = round(lado_c, 2)
   

    return lado_c


def tipo_triangulo(lado_a, lado_b, lado_c):
    lado_a = float(lado_a)
    lado_b = float(lado_b)
    lado_c = float(lado_c)

    if  lado_a == lado_b and lado_b == lado_c:
        return 'Equilátero' 
    if  lado_a!= lado_b and lado_a != lado_c and lado_c != lado_a:
        return 'Escaleno'
    if ((lado_a == lado_b) and  (lado_a != lado_c)) or ((lado_a != lado_b) and (lado_a == lado_c)):
        return 'Isósceles'

def run():

    menu = """"
    En este portal podrás descifrar los secretos que ocultan los triángulos: 
    Para encontrar el área, elige el número de opción que se ajusta a los datos que tienes:

    1. Si conoces la base (b)  y la altura (h).
    2. Si conoces la medida los tres lados.
    3. Si conoces el valor de dos lados y el del ángulo que está justo entre ellos.
    4. Si conoces el valor de un lado y el de los angulos adyacentes a él.

    Opción elegida:  """

    tipo_datos = input(menu)
       
    if tipo_datos == '1':
        
        altura = input('ingresar valor de la altura del trángulo (h): ')
        base = input('ingresar valor de la base del triángulo: ')
        area = calculo_con_base_y_altura(base, altura)
       
        print('el área del trángulo es: ' + area )
        print ('El tipo de triángulo es aún un misterio porque no entregaste datos suficientes para descifrarlo')
        
    elif tipo_datos == '2':
        lado_a = input('ingrese valor del lado a: ')
        lado_b = input('ingrese valor del lado b: ')
        lado_c = input('ingrese valor del lado c: ')
        area = calculo_con_tres_lados(lado_a, lado_b, lado_c)
        tipo = tipo_triangulo(lado_a, lado_b, lado_c)

        print('Es un triángulo ' + tipo + ' con un área de: ' + area  + ' unidades'  )

    elif tipo_datos == '3':

        lado_a = input('ingrese valor de un lado : ')
        lado_b = input('ingrese valor del otro lado : ')
        angulo_x = input('ingrese, en grados, el valor de ángulo que se forma justo entre los 2 lados conocidos: ')
        area = calculo_con_dos_lados_un_angulo(lado_a, lado_b, angulo_x)
        lado_c = calculo_de_lado_c_faltante(lado_a, lado_b, angulo_x)
        tipo = tipo_triangulo(lado_a, lado_b, lado_c)
        print(lado_c)

        print('Es un triángulo ' + tipo + ' con un área de: ' + area  + ' unidades'  )

    elif tipo_datos == '4':
        lado_a = input('ingrese lado conocido: ')
        angulo_y = input('ingrese, en grados,  valor del ángulo adyacente: ')
        angulo_x = input('ingrese, en grados, valor del otro ángulo adyacente: ')
        area = calculo_con_un_lado_dos_angulos(lado_a, angulo_x, angulo_y)
        lado_b = calculo_del_lado_b_faltante(lado_a, angulo_x, angulo_y)
        lado_c = calculo_del_lado_cc_faltante(lado_a, angulo_x, angulo_y)
        tipo = tipo_triangulo(lado_a, lado_b, lado_c)
        print(lado_b)
        print(lado_c)

        print('Es un triángulo ' + tipo + ' con un área de: ' + area  + ' unidades'  )

		else:
				print('Esa opción no existe, esccriba po favor una opción válida')    

if __name__ == '__main__':
    run()