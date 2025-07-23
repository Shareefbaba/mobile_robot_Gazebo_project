from launch import LaunchDescription
from launch_ros.actions import Node



def generate_launch_description():
    ld = LaunchDescription()

    number_publisher = Node(
        package="my_package",
        executable="number_publisher.py"
    )

    number_counter = Node(
        package="my_package",
        executable="number_sub_pub.py"
    )

    ld.add_action(number_publisher)
    ld.add_action(number_counter)
    
    return ld