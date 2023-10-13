from Game import all_functions
from NEAT import Gene_manager


def generate():
    gene_manager = Gene_manager.GeneManager()
    gene_manager.add_gene("frame", "sensor", all_functions.get_frame)
    gene_manager.add_gene("distance", "sensor", all_functions.get_distance)
    #gene_manager.add_gene("projectiles", "sensor", all_functions.get_projectiles)
    #gene_manager.add_gene("stage", "sensor", all_functions.get_stage)
    gene_manager.add_gene("ecb_bottom", "sensor", all_functions.get_ecb_bottom)
    gene_manager.add_gene("ecb_left", "sensor", all_functions.get_ecb_left)
    gene_manager.add_gene("ecb_right", "sensor", all_functions.get_ecb_right)
    gene_manager.add_gene("ecb_top", "sensor", all_functions.get_ecb_top)
    gene_manager.add_gene("position", "sensor", all_functions.get_position)
    gene_manager.add_gene("stock", "sensor", all_functions.get_stock)
    gene_manager.add_gene("percent", "sensor", all_functions.get_percent)
    #gene_manager.add_gene("action", "sensor", all_functions.get_action)
    gene_manager.add_gene("action_frame", "sensor", all_functions.get_action_frame)
    gene_manager.add_gene("facing", "sensor", all_functions.get_facing)
    gene_manager.add_gene("hitlag_left", "sensor", all_functions.get_hitlag_left)
    gene_manager.add_gene("hitstun_frames_left", "sensor", all_functions.get_hitstun_frames_left)
    gene_manager.add_gene("invulnerability_left", "sensor", all_functions.get_invulnerability_left)
    gene_manager.add_gene("invulnerable", "sensor", all_functions.get_invulnerable)
    gene_manager.add_gene("jumps_left", "sensor", all_functions.get_jumps_left)
    gene_manager.add_gene("moonwalkwarning", "sensor", all_functions.get_moonwalkwarning)
    gene_manager.add_gene("off_stage", "sensor", all_functions.get_off_stage)
    gene_manager.add_gene("on_ground", "sensor", all_functions.get_on_ground)
    gene_manager.add_gene("shield_strength", "sensor", all_functions.get_shield_strength)
    gene_manager.add_gene("speed_air_x_self", "sensor", all_functions.get_speed_air_x_self)
    gene_manager.add_gene("speed_ground_x_self", "sensor", all_functions.get_speed_ground_x_self)
    gene_manager.add_gene("speed_x_attack", "sensor", all_functions.get_speed_x_attack)
    gene_manager.add_gene("speed_y_attack", "sensor", all_functions.get_speed_y_attack)
    gene_manager.add_gene("speed_y_self", "sensor", all_functions.get_speed_y_self)
    gene_manager.add_gene("opponent_ecb_bottom", "sensor", all_functions.get_opponent_ecb_bottom)
    gene_manager.add_gene("opponent_ecb_left", "sensor", all_functions.get_opponent_ecb_left)
    gene_manager.add_gene("opponent_ecb_right", "sensor", all_functions.get_opponent_ecb_right)
    gene_manager.add_gene("opponent_ecb_top", "sensor", all_functions.get_opponent_ecb_top)
    gene_manager.add_gene("opponent_position", "sensor", all_functions.get_opponent_position)
    gene_manager.add_gene("opponent_stock", "sensor", all_functions.get_opponent_stock)
    gene_manager.add_gene("opponent_percent", "sensor", all_functions.get_opponent_percent)
    #gene_manager.add_gene("opponent_action", "sensor", all_functions.get_opponent_action)
    gene_manager.add_gene("opponent_action_frame", "sensor", all_functions.get_opponent_action_frame)
    gene_manager.add_gene("opponent_facing", "sensor", all_functions.get_opponent_facing)
    gene_manager.add_gene("opponent_hitlag_left", "sensor", all_functions.get_opponent_hitlag_left)
    gene_manager.add_gene("opponent_hitstun_frames_left", "sensor", all_functions.get_opponent_hitstun_frames_left)
    gene_manager.add_gene("opponent_invulnerability_left", "sensor", all_functions.get_opponent_invulnerability_left)
    gene_manager.add_gene("opponent_invulnerable", "sensor", all_functions.get_opponent_invulnerable)
    gene_manager.add_gene("opponent_jumps_left", "sensor", all_functions.get_opponent_jumps_left)
    gene_manager.add_gene("opponent_moonwalkwarning", "sensor", all_functions.get_opponent_moonwalkwarning)
    gene_manager.add_gene("opponent_off_stage", "sensor", all_functions.get_opponent_off_stage)
    gene_manager.add_gene("opponent_on_ground", "sensor", all_functions.get_opponent_on_ground)
    gene_manager.add_gene("opponent_shield_strength", "sensor", all_functions.get_opponent_shield_strength)
    gene_manager.add_gene("opponent_speed_air_x_self", "sensor", all_functions.get_opponent_speed_air_x_self)
    gene_manager.add_gene("opponent_speed_ground_x_self", "sensor", all_functions.get_opponent_speed_ground_x_self)
    gene_manager.add_gene("opponent_speed_x_attack", "sensor", all_functions.get_opponent_speed_x_attack)
    gene_manager.add_gene("opponent_speed_y_attack", "sensor", all_functions.get_opponent_speed_y_attack)
    gene_manager.add_gene("opponent_speed_y_self", "sensor", all_functions.get_opponent_speed_y_self)
    gene_manager.add_gene("random_input", "sensor", all_functions.get_random_input)
    gene_manager.add_gene("tilt_c_stick_x", "output", all_functions.tilt_c_stick_x)
    gene_manager.add_gene("tilt_c_stick_y", "output", all_functions.tilt_c_stick_y)
    gene_manager.add_gene("tilt_stick_x", "output", all_functions.tilt_stick_x)
    gene_manager.add_gene("tilt_stick_y", "output", all_functions.tilt_stick_y)
    gene_manager.add_gene("press_B", "output", all_functions.press_B)
    gene_manager.add_gene("press_A", "output", all_functions.press_A)
    gene_manager.add_gene("press_Y", "output", all_functions.press_Y)
    gene_manager.add_gene("press_X", "output", all_functions.press_X)
    gene_manager.add_gene("press_Z", "output", all_functions.press_Z)
    gene_manager.add_gene("press_L", "output", all_functions.press_L)
    gene_manager.add_gene("press_R", "output", all_functions.press_R)
    gene_manager.add_gene("do_nothing", "output", all_functions.do_nothing)
    return gene_manager
