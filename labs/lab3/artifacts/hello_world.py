import time
from datetime import datetime
import awsiot.greengrasscoreipc
import awsiot.greengrasscoreipc.client as client
from awsiot.greengrasscoreipc.model import (
    QOS,
    PublishToIoTCoreRequest
)

TIMEOUT = 10

ipc_client = awsiot.greengrasscoreipc.connect()
                    
topic = "test/topic"
qos = QOS.AT_LEAST_ONCE

request = PublishToIoTCoreRequest()
request.topic_name = topic
request.qos = qos

while (True):
    # Set message to grp_id/timestamp
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message = f"Group3: {timestamp}"
    request.payload = bytes(message, "utf-8")

    # Publish message
    operation = ipc_client.new_publish_to_iot_core()
    operation.activate(request)
    future = operation.get_response()
    future.result(TIMEOUT)

    # Sleep for 10 seconds
    time.sleep(10)
