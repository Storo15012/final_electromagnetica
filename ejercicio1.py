from vpython import canvas, vector, color, sphere, arrow, mag, box, cylinder, label

# Crear un lienzo VPython con un renderizador WebGL
scene = canvas(width=800, height=600, center=vector(0, 0, 0), background=color.white, title="Simulación de Campo Eléctrico")

# Escala para mejorar la visualización y constante de Coulomb
scale = 4e-14 / 1e17
kel = 9e9  

# Cargas en coordenadas (x, y, z) y sus respectivas cargas (en Coulombs)
cargas = [
    sphere(pos=vector(3, 2, -1), Q=1e-6, color=color.red, radius=0.1),
    sphere(pos=vector(-1, -1, 4), Q=-2e-6, color=color.blue, radius=0.1)
]

# Carga puntual en coordenadas (x, y, z) y su carga (en Coulombs)
carga_puntual = sphere(pos=vector(0, 3, 1), Q=10e-9, color=color.green, radius=0.1)

# Crear etiquetas para cada esfera
for carga in cargas:
    label(pos=carga.pos, text=f"Carga\n({carga.pos.x:.1f}, {carga.pos.y:.1f}, {carga.pos.z:.1f})", height=12, border=4)

label(pos=carga_puntual.pos, text=f"Carga Puntual\n({carga_puntual.pos.x:.1f}, {carga_puntual.pos.y:.1f}, {carga_puntual.pos.z:.1f})", color=color.green, xoffset=15, yoffset=15, height=12, border=4)

# Crear plano de suelo
suelo = box(pos=vector(0, -0.1, 0), size=vector(10, 0.1, 10), color=color.gray(0.7))

# Crear ejes XYZ
radio_ejes = 0.02
cylinder(pos=vector(0, 0, 0), axis=vector(1, 0, 0), color=color.red, radius=radio_ejes)
cylinder(pos=vector(0, 0, 0), axis=vector(0, 1, 0), color=color.green, radius=radio_ejes)
cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 1), color=color.blue, radius=radio_ejes)

# Función para calcular el campo eléctrico en un punto dado
def obtener_campo(p):
    campo = vector(0, 0, 0)
    for carga in cargas:
        campo = campo + (p - carga.pos) * kel * carga.Q / mag(p - carga.pos) ** 3
    return campo

# Función para actualizar la flecha que representa el campo eléctrico
def actualizar_flecha(flecha):
    raton_a_campo(flecha)

# Función para actualizar la flecha basada en la posición del ratón
def raton_a_campo(flecha):
    p = scene.mouse.pos
    campo = obtener_campo(p)
    m = mag(campo)
    rojo = max(1 - 1e17 / m, 0)
    azul = min(1e17 / m, 1)
    if rojo >= azul:
        azul = azul / rojo
        rojo = 1.0
    else:
        rojo = rojo / azul
        azul = 1.0
    flecha.pos = p
    flecha.axis = scale * campo
    flecha.color = vector(rojo, 0, azul)

    # Actualizar etiqueta con información del campo eléctrico
    etiqueta_campo.pos = p + vector(0, 0.2, 0)
    etiqueta_campo.text = f"Campo Eléctrico\n({campo.x:.2e}, {campo.y:.2e}, {campo.z:.2e}) N/C"

arrastrar = False
flecha = arrow(shaftwidth=0.01, color=color.black)  # Inicializar la flecha

# Etiqueta para información del campo eléctrico
etiqueta_campo = label(pos=vector(0, 0, 0), text="", height=12, border=4)

# Manejadores de eventos para la interacción con el ratón
def clic_abajo(ev):
    global flecha, arrastrar
    actualizar_flecha(flecha)
    arrastrar = True

def mover(ev):
    global flecha, arrastrar
    if not arrastrar: return
    actualizar_flecha(flecha)

def clic_arriba(ev):
    global flecha, arrastrar
    actualizar_flecha(flecha)
    arrastrar = False

# Vincular los manejadores de eventos a los eventos del ratón
scene.bind("mousedown", clic_abajo)
scene.bind("mousemove", mover)
scene.bind("mouseup", clic_arriba)

# Calcular la fuerza eléctrica en la carga puntual
fuerza_en_carga_puntual = vector(0, 0, 0)
for carga in cargas:
    fuerza_en_carga_puntual += (carga_puntual.pos - carga.pos) * kel * carga.Q * carga_puntual.Q / mag(carga_puntual.pos - carga.pos) ** 3

print(f"Fuerza eléctrica en la carga puntual: {fuerza_en_carga_puntual} N")

# Etiqueta para información de la fuerza eléctrica
etiqueta_fuerza = label(pos=carga_puntual.pos + vector(0, 0.2, 0), text=f"Fuerza Eléctrica\n({fuerza_en_carga_puntual.x:.2e}, {fuerza_en_carga_puntual.y:.2e}, {fuerza_en_carga_puntual.z:.2e}) N", height=12, border=4)

# Calcular el campo eléctrico en la carga puntual
campo_electrico_en_punto = obtener_campo(carga_puntual.pos)

print(f"Campo Eléctrico en la carga puntual: {campo_electrico_en_punto} N/C")

scene.waitfor("click")  # Esperar un clic para mantener abierta la visualización en ventana 