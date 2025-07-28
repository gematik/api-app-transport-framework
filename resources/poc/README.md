# Proof of Concept: App-Transport-Framework (ATF)

This PoC implements the requirements from https://simplifier.net/app-transport-framework and https://simplifier.net/guide/atf-implementation-guide?version=current.
The App-Transport-Framework (ATF) library that simplifies and standardizes the sending and receiving of FHIR messages. The ATF library allows developers to implement various use cases and provide custom handlers for processing FHIR messages.

## Benefits of the App-Transport-Framework

* Standardized FHIR message processing
* Easy integration with existing systems
* Extensibility through custom handlers
* Supports communication between various applications and services
* Simplifies the implementation of FHIR message processing in your applications
* Validates received FHIR resources and sends standardized acknowledgment messages to the sender
* Allows registering custom validation handlers for specific systems and use cases

## Using the ATF Library

In the following section, you will find an example of using the ATF library. The example demonstrates how to create an ``ATF_BundleProcessor`` to send and receive messages and how to use custom handlers for adding Validators (and issues) for usecase specific respond messages.

### Example File
The example file example.py demonstrates the basic usage of the ATF library. It contains the implementation of two ATF_BundleProcessor instances (sender and receiver) and demonstrates how to register custom handlers and access message contents.

To run the example, make sure you have installed all required dependencies and execute 
```cmd
python example.py
```

### Step-by-Step Guide

* Import the required modules and create sender and receiver references, as well as ``ATF_BundleProcessor`` instances for sender and receiver.

* Define custom functions (handlers) for processing message contents and receiving acknowledgments.

* Subscribe to the events of the ``ATF_BundleProcessor`` instances to access message contents and receive acknowledgments.

* Create a test message using the ``TestMessageCreator`` class and send the message to the receiver.

* Process the test message at the receiver and access the message content.

To register custom use case handlers, use the 
``atf.processor.register_use_case_handler`` method, providing a ``system``, ``code``, and ``handler``:
```python
def register_use_case_handler(self, system: str, code: str, handler: BaseUseCaseHandler):
    self.use_case_handlers[(system, code)] = handler
```

The advantage for the implementer is that, once the effort has been made to support the ATF framework, the validation and acknowledgment message exchange is implemented for all use cases.

For more information on implementing custom handlers and using the ATF library in your projects, please refer to the documentation and the example file example.py.