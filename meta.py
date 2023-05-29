import requests
import json

def get_aws_instance_metadata():
    response = requests.get('http://169.254.169.254/latest/dynamic/instance-identity/document')
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
cloud_provider = input("Enter the cloud provider (AWS): ")

if cloud_provider.lower() == "aws":
    metadata = get_aws_instance_metadata()
else:
    print("Invalid cloud provider.")
    exit(1)

if metadata:
    json_output = json.dumps(metadata, indent=4)
    print(json_output)
else:
    print("Failed to retrieve instance metadata.")
