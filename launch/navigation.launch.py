from os.path import join

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    pkg_path = get_package_share_directory('warehouse_navigation')

    map_file = join(pkg_path ,'maps' ,'warehouse_map.yaml')

    params_file = join(pkg_path,'config','nav2_params.yaml')

    nav2_bringup_dir = get_package_share_directory('nav2_bringup')

    bringup_launch = join(nav2_bringup_dir,'launch','bringup_launch.py')

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(bringup_launch),
        launch_arguments={
            'map': map_file,
            'use_sim_time': 'True',
            'params_file': params_file,
        }.items()
    )

    return LaunchDescription([
        nav2
    ])