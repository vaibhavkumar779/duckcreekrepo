import asyncio

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient

EVENT_HUB_CONNECTION_STR = "Endpoint=sb://eventhubnamesapce.servicebus.windows.net/;SharedAccessKeyName=RootUserAccessPolicy;SharedAccessKey=gsoJ6AK8nnbcAhzjHNR//uFMNzs+b6RtV5oFz8StJF0=;EntityPath=eventhubduck"
EVENT_HUB_NAME = "eventhubduck"

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.

    while True:
        await asyncio.sleep(1)

        producer = EventHubProducerClient.from_connection_string(
            conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME
        )
        async with producer:
            # Create a batch.
            event_data_batch = await producer.create_batch()

            # Add events to the batch.
            event_data_batch.add(EventData("First event "))
            event_data_batch.add(EventData("Second event"))
            event_data_batch.add(EventData("Third event"))

            # Send the batch of events to the event hub.
            await producer.send_batch(event_data_batch)
            print("sent to azure successfully")

loop = asyncio.get_event_loop()

try:
    asyncio.run(run())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing the loop")
    loop.close()