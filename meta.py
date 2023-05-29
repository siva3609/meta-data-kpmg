import requests
import json

def get_aws_instance_metadata():
    url = 'http://169.254.169.254/latest/meta-data/'
    response = requests.get(url)
    metadata = {}

    if response.status_code == 200:
        metadata['instance_id'] = response.text.strip()
        metadata['availability_zone'] = requests.get(url + 'placement/availability-zone').text.strip()
        metadata['instance_type'] = requests.get(url + 'instance-type').text.strip()
        metadata['public_ip'] = requests.get(url + 'public-ipv4').text.strip()
        metadata['private_ip'] = requests.get(url + 'local-ipv4').text.strip()

    return metadata

# Usage
aws_metadata = get_aws_instance_metadata()
json_output = json.dumps(aws_metadata, indent=4)
print(json_output)
