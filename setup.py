from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'warehouse_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),

    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),

        # Launch files
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')
        ),

        # Configuration files
        (
            os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')
        ),

        # World files
        (
            os.path.join('share', package_name, 'worlds'),
            glob('worlds/*.sdf')
        ),

        # URDF/Xacro files
        (
            os.path.join('share', package_name, 'urdf'),
            glob('urdf/*')
        ),

        # Map files
        (
            os.path.join('share', package_name, 'maps'),
            glob('maps/*')
        ),

        ('share/' + package_name + '/models/rack',
        glob('models/rack/*')),

    ],

    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='manoj',
    maintainer_email='manoj@todo.todo',

    description='Warehouse navigation simulation using ROS 2 Nav2',
    license='MIT',

    extras_require={
        'test': [
            'pytest',
        ],
    },

    entry_points={
        'console_scripts': [],
    },
)
