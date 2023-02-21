import turtle as t

# Réglage de la vitesse de dessin pour qu'il soit plus rapide
t.speed(5)
t.bgcolor('black')
def draw_apple(x, y, size):
    # Lever le stylo pour déplacer le turtle sans dessiner
    t.penup()
    t.goto(x, y)
    # Abaisser le stylo pour recommencer à dessiner
    t.pendown()
    
    # Définir la couleur du stylo en rouge
    t.pencolor("yellow")
    # Commencer à remplir la forme avec la couleur définie ci-dessus
    t.begin_fill()
    # Dessiner un cercle de la taille spécifiée
    t.circle(size)
    
    # Définir la couleur du stylo en blanc
    t.pencolor("#FFFFFF")
    # Commencer à remplir la forme avec la couleur définie ci-dessus
    t.begin_fill()
    # Dessiner un cercle de 80% de la taille du premier cercle
    t.circle(size * 0.8)
    draw_apple(x+1, y+2, size+20)

# Appeler la fonction pour dessiner le logo Apple
draw_apple(0, 0, -160)
# Afficher le dessin
turtle.done()
