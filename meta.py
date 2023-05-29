from azure.identity import DefaultAzureCredential                      #need to import the packages from azure
from azure.mgmt.compute import ComputeManagementClient

def get_azure_instance_metadata():
    credential = DefaultAzureCredential()
    subscription_id = 'YOUR_SUBSCRIPTION_ID'   #subscription details with owner access
    resource_group = 'YOUR_RESOURCE_GROUP'     # RG name under the subscription
    vm_name = 'YOUR_VM_NAME'

    client = ComputeManagementClient(credential, subscription_id)
    vm = client.virtual_machines.get(resource_group, vm_name, expand='instanceView')
    metadata = {
        'name': vm.name,
        'location': vm.location,
        'vm_size': vm.hardware_profile.vm_size,
       
    }
    return metadata

azure_metadata = get_azure_instance_metadata()
azure_metadata_json = json.dumps(azure_metadata, indent=4)
print(azure_metadata_json)
