def centrar_ventana(ventana, ancho, largo):
    ancho = ventana.wininfo_screenwidth()
    largo = ventana.wininfo_screenheight()
    x = int((ancho / 2) - (ancho / 2))
    y = int((largo / 2) - (largo / 2))
    return ventana.geometry(f"{ancho}x{largo}+{x}+{y}")
