from flask import Flask, jsonify
import boto3

app = Flask(__name__)
ec2 = boto3.resource('ec2')

@app.route('/ec2/instances', methods=['GET'])
def get_all_instances():
    instances = ec2.instances.all()
    instance_list = []
    for instance in instances:
        # 
        instance_dict = {
            'id': instance.id,
            'state': instance.state['Name'],
            'instance_type': instance.instance_type,
            'availability_zone': instance.placement['AvailabilityZone'],
            'security_groups': instance.security_groups,
            'private_ip': instance.private_ip_address,
            'public_ip': instance.public_ip_address,
            'launch_time': instance.launch_time.strftime("%Y-%m-%d %H:%M:%S"),
            # Add more attributes as needed
        }
        instance_list.append(instance_dict)
    return jsonify(instance_list)

@app.route('/ec2/instances/start', methods=['POST'])
def start_all_instances():
    instances = ec2.instances.all()
    instance_ids = [instance.id for instance in instances]
    ec2.instances.filter(InstanceIds=instance_ids).start()
    return jsonify({'message': 'EC2 instances are starting...'})

@app.route('/ec2/instances/stop', methods=['POST'])
def stop_all_instances():
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    instance_ids = [instance.id for instance in instances]
    ec2.instances.filter(InstanceIds=instance_ids).stop()
    return jsonify({'message': 'Running EC2 instances are stopping...'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8080"), debug=True)

