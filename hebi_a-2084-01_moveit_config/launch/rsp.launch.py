from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_rsp_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("A-2084-01", package_name="hebi_a-2084-01_moveit_config").to_moveit_configs()
    return generate_rsp_launch(moveit_config)