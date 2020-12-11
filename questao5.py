# Usando a biblioteca ‘turtle’ crie uma função que desenhe a imagem a seguir:
# Link imagem:
# https://lms.infnet.edu.br/moodle/pluginfile.php/732830/mod_assign/intro/KFo0wqEdT9Ju7-43Lhq8DDjLPXwXR-50_542fFGb7n3lTvDRwl7kSfCsyiipO4VSR39FV8v6R-xnd4yiQut4LAedKpby7459tDON-2Pmjuz-a9coKdPL91-6kx6HY7Uf6ASzv4Rs.jpg

import turtle

t = turtle.Turtle()

def draw_square(size_len):

    for i in range(4):
        t.forward(size_len)
        t.left(90)


def draw_square_filled():

    side = 400

    # Drawing the big square:
        # positioning the pen
    t.penup()
    t.backward(side/2)
    t.left(90)
    t.backward(side/2)
    t.right(90)
    t.pendown()

    draw_square(side)

    t.penup()
    t.forward((side/(3/4)) - 10)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()

    # t.circle((side/4) - 10)




draw_square_filled()