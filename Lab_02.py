import arcade

arcade.open_window(800, 600, "Apartment Buildings")
arcade.set_background_color(arcade.csscolor.DARK_BLUE)
arcade.start_render()
# moon
arcade.draw_circle_filled(550, 500, 140, (255, 247, 0, 127))
arcade.draw_circle_filled(550, 500, 100, arcade.csscolor.YELLOW)
# ground
arcade.draw_rectangle_filled(400, 50, 800, 150, arcade.csscolor.BLACK)
# building 1
arcade.draw_rectangle_filled(250, 300, 200, 400, arcade.csscolor.BLACK)
# building 2
arcade.draw_rectangle_filled(460, 300, 200, 500, arcade.csscolor.BLACK)
# windows
arcade.draw_rectangle_filled(400, 510, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(460, 510, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(520, 510, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(400, 450, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(460, 450, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(520, 450, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(400, 390, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(460, 390, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(520, 390, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(400, 330, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(400, 330, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(460, 330, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(520, 330, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(400, 270, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(460, 270, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(520, 270, 50, 50, arcade.csscolor.YELLOW)
# door
arcade.draw_rectangle_filled(460, 150, 30, 40, arcade.csscolor.GRAY)
# windows
arcade.draw_rectangle_filled(190, 460, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(250, 460, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(310, 460, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(250, 400, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(310, 400, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(190, 400, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(190, 340, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(250, 340, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(310, 340, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(190, 280, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(250, 280, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(310, 280, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(190, 220, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(250, 220, 50, 50, arcade.csscolor.YELLOW)
arcade.draw_rectangle_filled(310, 220, 50, 50, arcade.csscolor.YELLOW)
# bench
arcade.draw_rectangle_filled(140, 135, 5, 10, arcade.csscolor.BROWN)
arcade.draw_rectangle_filled(160, 135, 5, 10, arcade.csscolor.BROWN)
arcade.draw_rectangle_filled(150, 145, 30, 10, arcade.csscolor.DARK_GREY)
arcade.draw_rectangle_filled(150, 135, 30, 5, arcade.csscolor.DARK_GREY)
# tree
arcade.draw_triangle_filled(110, 190, 90, 140, 130, 140, arcade.csscolor.DARK_GREEN)
arcade.draw_rectangle_filled(110, 135, 5, 10, arcade.csscolor.BROWN)
# door
arcade.draw_rectangle_filled(250, 150, 30, 40, arcade.csscolor.GRAY)
# curb
arcade.draw_line(0, 120, 800, 120, (110, 110, 110), 20)
arcade.finish_render()
arcade.run()