from setuptools import setup

package_name = 'xsens_mti300_ahrs'

setup(
	name=package_name,
	version='0.0.0',
	packages=[package_name],
	data_files=[
		('share/ament_index/resource_index/packages',
			['resource/' + package_name]),
		('share/' + package_name, ['package.xml']),
	],
	install_requires=['setuptools'],
	zip_safe=True,
	maintainer='nontanan',
	maintainer_email='nontanan@todo.todo',
	description='TODO: Package description',
	license='TODO: License declaration',
	tests_require=['pytest'],
	entry_points={
		'console_scripts': [
			'xsense_driver = xsens_mti300_ahrs.imu_filter:main'
		],
	},
)
