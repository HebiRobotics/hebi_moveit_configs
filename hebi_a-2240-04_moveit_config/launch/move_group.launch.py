from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_move_group_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("A-2240-04", package_name="hebi_a-2240-04_moveit_config").to_moveit_configs()
    return generate_move_group_launch(moveit_config)
