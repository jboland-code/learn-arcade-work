import arcade
arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.csscolor.DARK_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.DARK_BLUE)
arcade.draw_text("N",
                 0, -100,
                 arcade.color.GOLD, 600)
arcade.draw_text("D",
                 -20, -50,
                 arcade.color.GOLD, 500, 1000)
arcade.draw_rectangle_filled(100, 320, 0, 60, arcade.csscolor.SIENNA)

arcade.finish_render()
arcade.run()