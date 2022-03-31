import time
import traceback

import awsiot.greengrasscoreipc
import awsiot.greengrasscoreipc.client as client
from awsiot.greengrasscoreipc.model import (
    IoTCoreMessage,
    QOS,
    PublishToIoTCoreRequest,
    SubscribeToIoTCoreRequest
)

TIMEOUT = 1

ipc_client = awsiot.greengrasscoreipc.connect()

sub_topic = "clients/rpi-50046/hello/world"
pub_topic = "test/average"

pub_qos = QOS.AT_LEAST_ONCE
sub_qos = QOS.AT_LEAST_ONCE

pub_request = PublishToIoTCoreRequest()
pub_request.topic_name = pub_topic
pub_request.qos = pub_qos

sub_request = SubscribeToIoTCoreRequest()
sub_request.topic_name = sub_topic
sub_request.qos = sub_qos

# First message to MQTT test/average
pub_request.payload = bytes('Hi, this is the task2 component!', "utf-8")
pub_operation = ipc_client.new_publish_to_iot_core()
pub_operation.activate(pub_request)
pub_future = pub_operation.get_response()
pub_future.result(TIMEOUT)
print("Published message to topic {}".format(pub_topic))

class StreamHandler(client.SubscribeToIoTCoreStreamHandler):
    def __init__(self):
        super().__init__()
        self.buffer = []

    def on_stream_event(self, event: IoTCoreMessage) -> None:
        try:
            message = str(event.message.payload, "utf-8")

            self.buffer.append(int(message))

            if len(self.buffer) == 5:
                average = sum(self.buffer) / 5
                average_str = f"Average: {average}"

                pub_request.payload = bytes(average_str, "utf-8")
                pub_operation = ipc_client.new_publish_to_iot_core()
                pub_operation.activate(pub_request)
                pub_operation.get_response()

                self.buffer = []


            # Handle message.
        except:
            traceback.print_exc()

    def on_stream_error(self, error: Exception) -> bool:
        # Handle error.
        return True  # Return True to close stream, False to keep stream open.

    def on_stream_closed(self) -> None:
        # Handle close.
        pass

handler = StreamHandler()
operation = ipc_client.new_subscribe_to_iot_core(handler)
future = operation.activate(sub_request)
future.result(TIMEOUT)

while (True):
    time.sleep(1)