from pyray import *

WIDTH = 1200
HEIGHT = 800

init_window(WIDTH, HEIGHT, 'Scene')

set_target_fps(60)


# Shaders
lambert_sky = load_shader(0, 'lambert_sky.glsl')
mouse_shader_loc = get_shader_location(lambert_sky, 'mouse')

while not window_should_close():
    begin_drawing()

    clear_background(BLACK)

    begin_shader_mode(lambert_sky)
    draw_rectangle(0, 0, WIDTH, HEIGHT, BLACK)
    set_shader_value(lambert_sky, mouse_shader_loc, get_mouse_position(), ShaderAttributeDataType.SHADER_ATTRIB_VEC2)
    end_shader_mode()


    end_drawing()

close_window()