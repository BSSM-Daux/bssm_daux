import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node



def generate_launch_description():
    package_name='bssm_daux' #<--- CHANGE ME


    # ros2 launch bssm_daux rsp.launch.py use_sim_time:=true 실행 명령어
    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # ros2 launch gazebo_ros gazebo.launch.py 커맨드 실행 명령어 
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
             )

    # ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity bot_name 실행 명령어
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot'],
                        output='screen')


    # 전체 실행 
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
    ])