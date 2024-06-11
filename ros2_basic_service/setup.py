from setuptools import setup

package_name = 'ros2_basic_service'

setup(
    name=package_name,
    version='0.2.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='jetsonai',
    author_email='jetsonai@jetsonai.co.kr',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Examples of minimal service servers using rclpy.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'srv_server = ros2_basic_service.srv_server:main',
            'srv_client = ros2_basic_service.srv_client:main',
        ],
    },
)
