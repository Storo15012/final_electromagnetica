from vpython import canvas, vector, color, sphere,cylinder, arrow, mag, box, label, norm

# Constantes
k = 8.99e9  # Constante electrostática en N m^2/C^2

# Posiciones de las cargas
pos_carga1 = vector(3, 0, -1)
pos_carga2 = vector(-2, 0, 0)
pos_carga_puntual = vector(0, 0, 0)

# Magnitudes de las cargas
q_carga1 = 2e-9  # 2 nC
q_carga2 = 4e-9  # 4 nC

# Calcula las fuerzas
r1 = pos_carga_puntual - pos_carga1
r2 = pos_carga_puntual - pos_carga2

fuerza_carga1 = k * q_carga1 * q_carga2 / mag(r1)**2 * norm(r1)
fuerza_carga2 = k * q_carga2 * q_carga1 / mag(r2)**2 * norm(r2)

fuerza_resultante = fuerza_carga1 + fuerza_carga2

# Visualización en VPython
scene = canvas(title="Fuerza Eléctrica", width=800, height=600)
"""
# Plano XY
plano_xy = box(pos=vector(0, 0, 0), size=vector(10, 0.1, 10), color=color.white)

# Ejes XYZ
eje_x = arrow(pos=plano_xy.pos, axis=vector(1, 0, 0), color=color.red, shaftwidth=0.05)
eje_y = arrow(pos=plano_xy.pos, axis=vector(0, 1, 0), color=color.green, shaftwidth=0.05)
eje_z = arrow(pos=plano_xy.pos, axis=vector(0, 0, 1), color=color.blue, shaftwidth=0.05)
"""
# Crear plano de suelo
suelo = box(pos=vector(0, -0.1, 0), size=vector(10, 0.1, 10), color=color.gray(0.7))

# Crear ejes XYZ
radio_ejes = 0.02
cylinder(pos=vector(0, 0, 0), axis=vector(1, 0, 0), color=color.red, radius=radio_ejes)
cylinder(pos=vector(0, 0, 0), axis=vector(0, 1, 0), color=color.green, radius=radio_ejes)
cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 1), color=color.blue, radius=radio_ejes)

# Cargas
carga1 = sphere(pos=pos_carga1, radius=0.1, color=color.red)
carga2 = box(pos=pos_carga2, size=vector(0.2, 0.2, 0.2), color=color.blue)
carga_puntual = sphere(pos=pos_carga_puntual, radius=0.1, color=color.green)

# Etiquetas de posición de cargas
label(pos=pos_carga1, text=f"Carga 1\nPosición: {pos_carga1}", xoffset=15, yoffset=15, space=30, height=10)
label(pos=pos_carga2, text=f"Carga 2\nPosición: {pos_carga2}", xoffset=15, yoffset=15, space=30, height=10)
label(pos=pos_carga_puntual, text=f"Carga Puntual\nPosición: {pos_carga_puntual}", xoffset=15, yoffset=15, space=30, height=10)

# Flechas de fuerza
flecha_carga1 = arrow(pos=pos_carga_puntual, axis=fuerza_carga1, color=color.red)
flecha_carga2 = arrow(pos=pos_carga_puntual, axis=fuerza_carga2, color=color.blue)
flecha_resultante = arrow(pos=pos_carga_puntual, axis=fuerza_resultante, color=color.green)

# Etiqueta de la fuerza resultante
label(pos=flecha_resultante.pos + flecha_resultante.axis + vector(1, 0, 0), text=f"Fuerza Resultante:\n{fuerza_resultante}", xoffset=15, yoffset=15, space=30, height=10)

# Imprime el resultado por consola
print("Fuerza Resultante:", fuerza_resultante)

# Espera a que se cierre la ventana de VPython
scene.waitfor('click')
