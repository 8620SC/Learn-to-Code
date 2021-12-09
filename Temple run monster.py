import arcade

x = 300
y = 300


def draw_monkey(x, y):
    # Draws demon monkey
    arcade.start_render()
    arcade.draw_ellipse_filled(x, y - 280, 700, 700, arcade.color.BLACK)
    arcade.draw_circle_filled(x, y, 100, arcade.color.BLACK)
    arcade.draw_circle_filled(x, y + 40, 50, arcade.color.WHITE)
    arcade.draw_rectangle_filled(x, y - 20, 40, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 30, y + 40, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 30, y + 40, 20, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x + 10, y - 40, 10, 50, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x - 10, y - 40, 10, 50, arcade.color.BLACK)
    arcade.finish_render()


def movement():
    # Moves monkey
    x = 300
    y = 300
    while True:
        for i in range(100):
            draw_monkey(x, y)
            y -= 0.1
        for i in range(100):
            draw_monkey(x, y)
            y += 0.1


def main():
    arcade.open_window(600, 600, "Angry Demon Monkey")

    arcade.set_background_color(arcade.csscolor.WHITE)

    draw_monkey(x, y)

    movement()

    arcade.run()


main()


