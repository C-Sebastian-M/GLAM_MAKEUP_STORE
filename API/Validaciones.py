
def validar_NombreCom(nombre)->bool:
    nombre=str(nombre)
    nombreS = nombre.replace(" ", "")
    if nombreS.isalpha():
            return True
    return False

  #Validar cedula
def validar_Cedula(cedula)->bool:
        cedula=str(cedula)
        if len(str(cedula)) <7 or  len(str(cedula)) >=12:
            return False
        elif not cedula.isdigit():
            return False
        return True

  #Validar telefono
def validacion_Telefono(telefono)->bool:
    telefono = str(telefono)
    if len(telefono) == 10 and telefono.isdigit():
        return True
    return False

  #Validar referencia
def validacion_Referencia(referencia)->bool:
    referencia = str(referencia)
    if len(referencia) >= 2 and len(referencia) <= 12:
        return True
    else:
        return False

  #Validar codigo de barras
def validacion_Codigo_Barras(codigo)->bool:
    codigo=str(codigo)
    if len(codigo) == 13 and codigo.isdigit():
        return True
    else:
        return False

  #Validar marca
def validacion_Marca(marca)->bool:
    marca=str(marca)
    if marca.isalpha():
        return True
    else:
        return False

  #Validar precio
def validacion_Precio(precio_adquisicion)->bool:
    try:
        precio = float(precio_adquisicion)
        if precio > 0:
            return True
        else:
            return False
    except ValueError:
        return False

  #validar nombre usuario
def usuario(usuario):
    usuario = str(usuario)
    for caracter in usuario:
        if not (caracter.isalnum()):  # isalnum() retorna True si el carácter es alfanumérico (letra o número)
          return False
    return True

  #validar contraseña que tenga 8 o mas caracteres
def contraseña(contra):
    contra = str(contra)
    if len(contra)>= 8:
      return True
    return False

  #verifica si el nombre del servicio solo es alfabetico
def validar_NombreServ(nombre)->bool:
    nombre=str(nombre)
    nombreS = nombre.replace(" ", "")
    if nombreS.isalpha():
            return True
    return False

  #verifica si el usuario es administrador o cliente
def rol(papel):
    if papel == "administrador" or papel == "Administrador" or "ADMINISTRADOR":
      return True
    return False

  #Validar que el costo sea un valor positivo
def validacion_Precio(costo)->bool:
        costo = float(costo)
        if costo > 0:
            return True
        return False
def validar_NombreCli(nombre):
    nombre = str(nombre)
    nombreS = nombre.replace(" ", "")
    if nombreS.isalpha():
      return True
    return False

  #Validar servicio
def validacion_Servicio(servicio):
    servicio = str(servicio)
    servicioS = servicio.replace(" ", "")
    if servicioS.isalpha():
      return True
    return False

  #Validar costo
def validacion_Costo(costo_servicio):
    try:
        costo = float(costo_servicio)
        if costo > 0:
              return True
        else:
              return False
    except ValueError:
          return False
  #Validacion producto
def validacion_Producto(producto):
      producto = str(producto)
      if producto.isalpha():
          return True
      else:
          return False

 #Validar que el stock  positivo
def validacion_Stock( x)->bool:
        x = float(x)
        if x > 0:
            return True
        return False

  #Validar Producto
def validar_producto(producto)->bool:
    producto=str(producto)
    producto = producto.replace(" ", "")
    if producto.isalpha():
            return True
    return False

  #validar cantidad
def validar_cantidad(cantidad)->bool:
    try:
      cantidad = int(cantidad)
      if cantidad > 0:
        return True
      else:
        return False
    except:
      return False
#a
