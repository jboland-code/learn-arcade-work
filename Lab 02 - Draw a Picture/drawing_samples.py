import arcade
arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(arcade.csscolor.DARK_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 100, 100, 0, arcade.csscolor.DARK_BLUE)
arcade.draw_text("N",
                 0, 0,
                 arcade.color.GOLD, 450, 400)
arcade.draw_text("D",
                 0, 0,
                 arcade.color.GOLD, 450, 400)
arcade.draw_rectangle_filled(100, 320, 0, 60, arcade.csscolor.SIENNA)

arcade.finish_render()
arcade.run()