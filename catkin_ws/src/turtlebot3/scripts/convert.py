import rosbag
import yaml

bag_path = '/home/pc/catkin_ws/src/turtlebot3/bagfiles/2023-08-27-10-33-19.bag'
output_yaml_path = '/home/pc/catkin_ws/src/turtlebot3/output_data.yaml'

data_to_save = []

with rosbag.Bag(bag_path, 'r') as bag:
    for topic, msg, t in bag.read_messages(topics=['/cmd_vel']):
        # Extract the data you want and format it as a dictionary
        data_entry = {
            'timestamp': t.to_sec(),
            'value': msg.data  # Replace with the actual data field you want
        }
        data_to_save.append(data_entry)

# Write the data to a YAML file
with open(output_yaml_path, 'w') as yaml_file:
    yaml.dump(data_to_save, yaml_file)
