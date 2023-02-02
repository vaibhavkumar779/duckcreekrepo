from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

credential = DefaultAzureCredential()
subscription_id = "0600d38a-5064-48c7-a6aa-99a7ebc788f9"

client = ResourceManagementClient(credential, subscription_id)

resource_group_list = client.resource_groups.list()

for item in resource_group_list:
    print("{}\n".format(item.name))