import asyncio

from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import (
    BlobCheckpointStore,
)

BLOB_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=knoldusstorage;AccountKey=5momS1nQNQ57YZR9povJ4B+YM/NucLRNI9fASicqwKimKZLEP4hW6qgah2nnmZTAIj4i5b+cKvdA+AStHEclsg==;EndpointSuffix=core.windows.net"
BLOB_CONTAINER_NAME = "knoldusblob"
EVENT_HUB_CONNECTION_STR = "Endpoint=sb://knolduseventhub.servicebus.windows.net/;SharedAccessKeyName=RootPolicyAccess;SharedAccessKey=qq54G24WIEzmupDsKSEHE4cDoDUmqpLzjR6uRqH5uDA=;EntityPath=knoldusevent"
EVENT_HUB_NAME = "knoldusevent"

async def on_event(partition_context, event):
    # Print the event data.
    print(
        'Received the event: "{}" from the partition with ID: "{}"'.format(
            event.body_as_str(encoding="UTF-8"), partition_context.partition_id
        )
    )

    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    await partition_context.update_checkpoint(event)

async def main():
    # Create an Azure blob checkpoint store to store the checkpoints.
    checkpoint_store = BlobCheckpointStore.from_connection_string(
        BLOB_STORAGE_CONNECTION_STRING, BLOB_CONTAINER_NAME
    )

    # Create a consumer client for the event hub.
    client = EventHubConsumerClient.from_connection_string(
        EVENT_HUB_CONNECTION_STR,
        consumer_group="$Default",
        eventhub_name=EVENT_HUB_NAME,
        checkpoint_store=checkpoint_store,
    )
    async with client:
        # Call the receive method. Read from the beginning of the
        # partition (starting_position: "-1")
        await client.receive(on_event=on_event, starting_position="-1")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # Run the main method.
    
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing the loop")
        loop.close()