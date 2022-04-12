# Quiz 4

> James Raphael Tiovalen / 1004555

1. In FreeRTOS, the kernel scheduler kicks in immediately in the following moment(s). Note that this question can contain one or multiple correct answer(s), and you need to select all correct answer(s) in order to get the marks. No partial credit will be awarded.
   - [x] A tick interrupt happens.
   - [x] The current running task is suspended.
   - [x] The current running task is blocked.
   - [x] The current running task successfully takes a mutex.
2. Lab 1 uses presigned URL with a short expiration time to access the Amazon S3 service. This follows the security principle of:
   - Secure and fail-safe defaults
   - **Minimum exposure**
   - Application of STRIDE threat modeling
   - Two-way authentication
3. When an ESP32 device boots, it first executes the code from `_____`, then it loads the code from `_____` into `_____`.
   - SRAM, ROM, Flash
   - ROM, Flash, SRAM
   - SRAM, ROM, Flash
   - Flash, ROM, SRAM
4. One should use edge computing to process data locally only if the locally generated data are too bulky to be transferred to the cloud, or the round-trip time cannot meet the latency requirement. For small amount of data that do not have strict latency requirement for processing, it is always better to use the cloud directly. This is because the cloud provides lower cost and more flexibility compared to the use of edge-based solutions.
   - True
   - **False**
5. Which of the following statement(s) regarding AWS IoT Greengrass is/are true? Note that this question can contain one or multiple correct answer(s), and you need to select all correct answer(s) in order to get the marks. No partial credit will be awarded.
   - [x] AWS IoT Greengrass supports running Lambda function and MQTT service locally.
   - [ ] AWS IoT Greengrass is an integrated solution that consists of software and hardware, both supplied by AWS.
   - [x] AWS IoT Greengrass consists of both client side software and cloud side service.
   - [ ] AWS IoT Greengrass supports remote deployment of a custom component to a group of edge devices, but all devices in a group need to be based on the same Operating System and have pre-installed Greengrass nucleus component.
6. As its name suggests, an RTOS can schedule its tasks to complete faster than a non-real-time OS.
   - True
   - **False**
7. Priority inheritance is a technique that can mitigate the undesirable priority inversion when processes with different priority level need to use mutex to coordinate their access to a shared resource, however, priority inheritance cannot totally eliminate the priority inversion.
   - **True**
   - False
8. In the "PWN the ESP32" attack via voltage fault injection (as discussed in the lecture), the `_____` of the `_____` keys stored in the eFuse are compromised.
   - confidentiality, public
   - **confidentiality, symmetric**
   - integrity, public
   - integrity, symmetric
9. In FreeRTOS, the tick period is fixed by the hardware, though different hardware can have different tick period.
   - True
   - **False**
