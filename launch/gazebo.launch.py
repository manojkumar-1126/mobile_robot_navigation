from os.path import join

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, AppendEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    pkg_path = get_package_share_directory('warehouse_navigation')

    world_path = join(
        pkg_path,
        'worlds',
        'warehouse_world.sdf'
    )

    gz_sim_share = get_package_share_directory('ros_gz_sim')

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            join(
                gz_sim_share,
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={
            'gz_args': '-r ' + world_path
        }.items()
    )

    spawn_robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            join(
                pkg_path,
                'launch',
                'turtle_bot.launch.py'
            )
        )
    )

    return LaunchDescription([

        AppendEnvironmentVariable(
            name='IGN_GAZEBO_RESOURCE_PATH',
            value=join(pkg_path, 'models')
        ),

        gz_sim,
        spawn_robot
    ])
