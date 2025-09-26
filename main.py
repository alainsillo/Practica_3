import turtle

# ESPECIFICACIONES DE COLORES
palette = {
    0: "#fff0f5",  # Lavender Blush
    1: "#ffb6c1",  # Light Pink
    2: "#ff69b4",  # Hot Pink
    3: "#ff1493",  # Deep Pink
    4: "#db7093",  # Pale Violet Red
    5: "#c71585",  # Medium Violet Red
    6: "#ff007f",  # Bright Pink
    7: "#8b008b",  # Dark Magenta
    8: "#4b0082",  # Indigo Rosado
}

# CONFIGURACIÓN DE VENTANA
turtle.setup(width=800, height=800)
turtle.bgcolor("white")
turtle.speed(0)
turtle.hideturtle()
turtle.colormode(255)
turtle.tracer(0, 0)


# CARGA DE MATRIZ DESDE ARCHIVO
matriz = []
with open("pixel_art_100x100.txt", "r") as f:
    for line in f:
        fila = [int(x) for x in line.split()]
        matriz.append(fila)


# DIBUJO DE LA MATRIZ
pixel_size = 5

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        color = palette.get(matriz[i][j], "#000000")
        turtle.penup()
        x = -250 + j * pixel_size
        y = 250 - i * pixel_size
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(pixel_size)
            turtle.right(90)
        turtle.end_fill()

turtle.update()
turtle.done()

