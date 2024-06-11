from setuptools import find_packages
import os
from glob import glob
from setuptools import setup

package_name = 'ros2_basic_test'

setup(
    name=package_name,
    version='0.6.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))) 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='jetsonai',
    author_email='jetsonai@jetsonai.co.kr',
    maintainer='Pyo',
    maintainer_email='passionvirus@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='ROS 2 rclpy basic package for the ROS 2 seminar',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rostopic_pub = ros2_basic_test.rostopic_pub:main',
            'rostopic_sub = ros2_basic_test.rostopic_sub:main',
        ],
    },
)
