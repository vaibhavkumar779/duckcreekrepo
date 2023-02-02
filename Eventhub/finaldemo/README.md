# Requirements

1. Add Event Hub Namespace, EventHub
2. Azure Stream Analytics to see what is being streamed as we are using basic tier which does not let us to capture data in eventhub
3. recieve.py wcan be used to access the inputs provided

## Steps to run command

## 1. create python virtual_env

    ```
    command : python3 -m venv ./venv
    activation : source ./venv/bin/activate
    ```

## 2. install dependencies

    ```command: pip3 -r install ./requirements.txt```

## References

1. Creating the Eventhub Namespace
<https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-create>

2. Script for event
<https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-python-get-started-send?tabs=passwordless%2Croles-azure-portal>

3. Passwordless Connection
<https://learn.microsoft.com/en-us/azure/developer/intro/passwordless-overview>

4. Storage Account
<https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal>

5. Blob Container
<https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal>

6. youtube video reference
<https://youtu.be/-ImscAXAZj0>
