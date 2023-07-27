from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_warehouse_db_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("A-2085-05", package_name="hebi_a-2085-05_moveit_config").to_moveit_configs()
    return generate_warehouse_db_launch(moveit_config)
