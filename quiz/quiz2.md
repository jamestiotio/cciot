# Quiz 2

> James Raphael Tiovalen / 1004555

1. AWS Kinesis is typically used in which logical layer of an IoT system?
   - Edge Layer
   - Provisioning Layer
   - Communication Layer
   - **Ingestion Layer**
   - Analytics Layer
2. A sensor can have different sensitivity value at different subranges of its full scale range.
   - **True**
   - False
3. Which of the following can be used to subscribe to the following MQTT topic: `myhome/groundfloor/livingroom/temperature`? There can be one or multiple correct answer(s).
   - [ ] `myhome/#/temperature`
   - [x] `myhome/+/livingroom/temperature`
   - [ ] `+/livingroom/temperature`
   - [ ] `MYHOME/groundfloor/livingroom/temperature`
   - [x] `+/+/livingroom/temperature`
4. Calibration is the process of removing Additive White Gaussian Noise (AWGN) from a sensor's measurement, using some calibration standard of known accuracy.
   - True
   - **False**
5. Which of the following is/are needed for an AWS IoT registered thing to use an MQTT client to directly connect to the AWS IoT core message broker and **receive** messages of a specific topic? (Hint: Recall the steps you have taken to accomplish Lab 1 Part 1.)
   - [x] The thing's certificate
   - [x] A policy that attaches to the thing in AWS IoT core and grants permission to connect to AWS IoT Core message broker using the thing's chosen client ID
   - [x] A policy that attaches to the thing in AWS IoT core and grants permission to subscribe to the specific topic (or a wildcard topic name that matches the specific topic)
   - [ ] A policy that attaches to the thing in AWS IoT core and grants permission to publish to the specific topic (or a wildcard topic name that matches the specific topic)
   - [x] A policy that attaches to the thing in AWS IoT core and grants permission to receive messages of the specific topic (or a wildcard topic name that matches the specific topic)
   - [x] The thing's private key
6. All types of RAM are volatile memory while all types of ROM are non-volatile.
   - True
   - **False**
7. As ESP32 has only two I<sup>2</sup>C controllers, it can connect to maximum 2 external sensors over I<sup>2</sup>C.
   - True
   - **False**
8. For MQTT Version 3.1.1, a client can subscribe to a topic even if no one (including itself) has published any message to that topic. Similarly, a client can publish to a topic that no one (including itself) has subscribed to.
   - **True**
   - False
9. Both I<sup>2</sup>C and UART are serial communication technologies. One difference is that I<sup>2</sup>C must have a clock line while UART can operate without a clock line.
   - **True**
   - False
10. Compare two brands of sensors that measure the same physical phenomenon. The more accurate sensor is also always more precise.
    - True
    - **False**
11. Both I<sup>2</sup>C and SPI support full-duplex operation.
    - True
    - **False**