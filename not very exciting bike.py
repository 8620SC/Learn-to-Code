import arcade


def wheel(x, y):
    # draws wheel
    arcade.draw_circle_filled(x, y, 50, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(x, y, 40, arcade.csscolor.DARK_GREY)
    arcade.draw_ellipse_filled(x, y - 25, 40, 20, arcade.csscolor.SKY_BLUE)
    arcade.draw_ellipse_filled(x, y + 25, 40, 20, arcade.csscolor.SKY_BLUE)
    arcade.draw_circle_filled(x, y, 15, arcade.csscolor.BLACK)


def draw_body(x, y):
    arcade.draw_rectangle_filled(x, y, 40, 20, arcade.csscolor.BLACK, tilt_angle=350)
    arcade.draw_circle_filled(x + 30, y - 100, 15, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(x - 50, y - 50, 200, 90, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(x - 50, y - 60, 200, 10, arcade.csscolor.BLACK)
    arcade.draw_rectangle_filled(x - 140, y - 30, 20, 30, arcade.csscolor.WHITE)
    arcade.draw_line(x - 105, y + 45, x - 50, y + 45, arcade.csscolor.BLACK, line_width=8)


def draw_motocompo(x, y):
    arcade.draw_line(x - 150, y - 100, x - 100, y + 50, arcade.csscolor.BLACK, line_width=10)
    wheel(x + 30, y - 100)
    wheel(x - 150, y - 100)
    draw_body(x, y)
    arcade.draw_rectangle_filled(x + 50, y - 30, 20, 30, arcade.csscolor.DARK_RED)


def on_draw(delta_time):
    arcade.start_render()

    draw_motocompo(on_draw.motocompo_x, 350)
    draw_motocompo(on_draw.motocompo2_x, 350)
    on_draw.motocompo_x += -1
    on_draw.motocompo2_x += -1
    if on_draw.motocompo_x == 200:
        arcade.finish_render()
    if on_draw.motocompo2_x == 300:
        on_draw.motocompo2_x -= 1


on_draw.motocompo_x: int = 500
on_draw.motocompo2_x: int = 600


def main():
    arcade.open_window(600, 600, "Motocompo")
    arcade.set_background_color(arcade.csscolor.SKY_BLUE)

    arcade.schedule(on_draw, 1 / 120)

    arcade.run()


main()
