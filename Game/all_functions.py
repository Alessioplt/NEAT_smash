import random
import melee


def flatten_position(x, y):
    return x + y


def get_frame(game_state):
    return game_state.frame


def get_distance(game_state):
    return game_state.distance


def get_projectiles(game_state):
    if len(game_state.projectiles) < 1:
        return game_state.projectiles
    coord = game_state.projectiles[0].position
    coord = flatten_position(coord[0], coord[1])
    return coord


def get_stage(game_state):
    return game_state.stage


def get_ecb_bottom(game_state):
    coord = game_state.players[1].ecb_bottom
    coord = flatten_position(coord[0], coord[1])
    return coord


def get_ecb_left(game_state):
    coord = game_state.players[1].ecb_left
    coord = flatten_position(coord[0], coord[1])
    return coord


def get_ecb_right(game_state):
    coord = game_state.players[1].ecb_right
    coord = flatten_position(coord[0], coord[1])
    return coord


def get_ecb_top(game_state):
    coord = game_state.players[1].ecb_top
    coord = flatten_position(coord[0], coord[1])
    return coord


def get_position(game_state):
    coord = game_state.players[1].position
    coord = flatten_position(coord.x, coord.y)
    return coord


def get_stock(game_state):
    return game_state.players[1].stock


def get_percent(game_state):
    return game_state.players[1].percent


def get_action(game_state):
    return game_state.players[1].action.value


def get_action_frame(game_state):
    return game_state.players[1].action_frame


def get_facing(game_state):
    if game_state.players[1].facing:
        return 1
    return -1


def get_hitlag_left(game_state):
    if game_state.players[1].hitlag_left:
        return 1
    return -1


def get_hitstun_frames_left(game_state):
    return game_state.players[1].hitstun_frames_left


def get_invulnerability_left(game_state):
    return game_state.players[1].invulnerability_left


def get_invulnerable(game_state):
    if game_state.players[1].invulnerable:
        return 1
    return -1


def get_jumps_left(game_state):
    return game_state.players[1].jumps_left


def get_moonwalkwarning(game_state):
    if game_state.players[1].moonwalkwarning:
        return 1
    return -1


def get_off_stage(game_state):
    if game_state.players[1].off_stage:
        return 1
    return -1


def get_on_ground(game_state):
    if game_state.players[1].on_ground:
        return 1
    return -1


def get_shield_strength(game_state):
    return game_state.players[1].shield_strength


def get_speed_air_x_self(game_state):
    return game_state.players[1].speed_air_x_self


def get_speed_ground_x_self(game_state):
    return game_state.players[1].speed_ground_x_self


def get_speed_x_attack(game_state):
    return game_state.players[1].speed_x_attack


def get_speed_y_attack(game_state):
    return game_state.players[1].speed_y_attack


def get_speed_y_self(game_state):
    return game_state.players[1].speed_y_self


def get_opponent_ecb_bottom(game_state):
    coord = game_state.players[4].ecb_bottom
    coord = flatten_position(coord[0], coord[1])
    return coord


def get_opponent_ecb_left(game_state):
    coord = game_state.players[4].ecb_left
    coord = flatten_position(coord[0], coord[1])
    return coord


def get_opponent_ecb_right(game_state):
    coord = game_state.players[4].ecb_right
    coord = flatten_position(coord[0], coord[1])
    return coord


def get_opponent_ecb_top(game_state):
    coord = game_state.players[4].ecb_top
    coord = flatten_position(coord[0], coord[1])
    return coord


def get_opponent_position(game_state):
    coord = game_state.players[4].position
    coord = flatten_position(coord.x, coord.y)
    return coord


def get_opponent_stock(game_state):
    return game_state.players[4].stock


def get_opponent_percent(game_state):
    return game_state.players[4].percent


def get_opponent_action(game_state):
    return game_state.players[4].action


def get_opponent_action_frame(game_state):
    return game_state.players[4].action_frame


def get_opponent_facing(game_state):
    if game_state.players[4].facing:
        return 1
    return -1


def get_opponent_hitlag_left(game_state):
    if game_state.players[4].hitlag_left:
        return 1
    return -1


def get_opponent_hitstun_frames_left(game_state):
    return game_state.players[4].hitstun_frames_left


def get_opponent_invulnerability_left(game_state):
    return game_state.players[4].invulnerability_left


def get_opponent_invulnerable(game_state):
    if game_state.players[4].invulnerable:
        return 1
    return -1


def get_opponent_jumps_left(game_state):
    return game_state.players[4].jumps_left


def get_opponent_moonwalkwarning(game_state):
    if game_state.players[4].moonwalkwarning:
        return 1
    return -1


def get_opponent_off_stage(game_state):
    if game_state.players[4].off_stage:
        return 1
    return -1


def get_opponent_on_ground(game_state):
    if game_state.players[4].on_ground:
        return 1
    return -1


def get_opponent_shield_strength(game_state):
    return game_state.players[4].shield_strength


def get_opponent_speed_air_x_self(game_state):
    return game_state.players[4].speed_air_x_self


def get_opponent_speed_ground_x_self(game_state):
    return game_state.players[4].speed_ground_x_self


def get_opponent_speed_x_attack(game_state):
    return game_state.players[4].speed_x_attack


def get_opponent_speed_y_attack(game_state):
    return game_state.players[4].speed_y_attack


def get_opponent_speed_y_self(game_state):
    return game_state.players[4].speed_y_self


def get_random_input(game_state):
    return random.uniform(-1.0, 1.0)


# actions
def tilt_c_stick_x(controller):
    controller.tilt_analog(melee.enums.Button.BUTTON_C, 0.5, 0)


def tilt_c_stick_y(controller):
    controller.tilt_analog(melee.enums.Button.BUTTON_C, 0.5, 0)


def tilt_stick_x(controller):
    controller.tilt_analog(melee.enums.Button.BUTTON_MAIN, 0.5, 0)


def tilt_stick_y(controller):
    controller.tilt_analog(melee.enums.Button.BUTTON_MAIN, 0, 0)


def press_B(controller):
    controller.press_button(melee.enums.Button.BUTTON_B)


def press_A(controller):
    controller.press_button(melee.enums.Button.BUTTON_A)


def press_Y(controller):
    controller.press_button(melee.enums.Button.BUTTON_Y)


def press_X(controller):
    controller.press_button(melee.enums.Button.BUTTON_X)


def press_Z(controller):
    controller.press_button(melee.enums.Button.BUTTON_Z)


def press_L(controller):
    return controller.press_button(melee.enums.Button.BUTTON_L)


def press_R(controller):
    return controller.press_button(melee.enums.Button.BUTTON_R)


def do_nothing(controller):
    return controller.release_all()
