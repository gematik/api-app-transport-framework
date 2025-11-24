<img align="right" width="200" height="37" src="Gematik_Logo_Flag.png"/> <br/>

# API App Transport Framework (ATF) FHIR-Profiles

The ATF (App-Transport-Framework) is an open and independent framework designed to improve the efficiency of communication in medical services. It is based on structured data exchange using FHIR standards and aims to optimize communication through standardization and partial automation.

The profiles in this repository serve as a foundation for various use cases where medical data is exchanged via messaging services like KIM and TIM. The framework allows for automation of messaging processes without manual intervention, ensuring that messages are processed reliably and consistently.

Resources are published on [Simplifier](https://simplifier.net/app-transport-framework).

## Key Features

- **Open Framework**: The ATF is not restricted to specific use cases and can be applied flexibly across different domains.
- **FHIR-Based Communication**: Uses FHIR standards for structured and standardized communication between medical systems.
- **Decentralized and Scalable**: Supports both centralized and decentralized communication, making it adaptable for various medical settings like hospitals, pharmacies, and laboratories.
- **Layered OSI Model Integration**: The ATF operates primarily in the application layer (Layer 7) of the OSI model, defining how messages are structured and processed.
- **Partial Automation**: Designed to enable partial automation of message exchanges, reducing the need for manual interaction and improving efficiency.

## Information
For more detailed information about the ATF, refer to the following presentations:

- [Short Slide Deck](https://gematik.github.io/api-app-transport-framework/slides/atf-presentation/ATF_Presentation_Short.html)
- [Detailed Slide Deck](https://gematik.github.io/api-app-transport-framework/slides/atf-presentation/ATF_Presentation_Detail.html)

## About the Project

This repository contains FHIR Shorthand (FSH) files that will later be published on [Simplifier](https://simplifier.net/app-transport-framework). These files define the structure and implementation details for the ATF, supporting use cases like prescription requests, patient records management, and more.

### Project Goals

- **Structured Medical Communication**: Improve the flow of information between healthcare providers.
- **Automation of Processes**: Automate repetitive tasks and minimize manual intervention in messaging workflows.
- **Enhanced Interoperability**: Promote interoperability between different healthcare systems using FHIR and open standards.

## Contributing

We welcome contributions to the project. If you'd like to contribute, please check out our [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

Copyright 2023-2025 gematik GmbH

Apache License, Version 2.0

See the [LICENSE](./LICENSE) for the specific language governing permissions and limitations under the License

## Additional Notes and Disclaimer from gematik GmbH

1. Copyright notice: Each published work result is accompanied by an explicit statement of the license conditions for use. These are regularly typical conditions in connection with open source or free software. Programs described/provided/linked here are free software, unless otherwise stated.
2. Permission notice: Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    1. The copyright notice (Item 1) and the permission notice (Item 2) shall be included in all copies or substantial portions of the Software.
    2. The software is provided "as is" without warranty of any kind, either express or implied, including, but not limited to, the warranties of fitness for a particular purpose, merchantability, and/or non-infringement. The authors or copyright holders shall not be liable in any manner whatsoever for any damages or other claims arising from, out of or in connection with the software or the use or other dealings with the software, whether in an action of contract, tort, or otherwise.
    3. We take open source license compliance very seriously. We are always striving to achieve compliance at all times and to improve our processes. If you find any issues or have any suggestions or comments, or if you see any other ways in which we can improve, please reach out to: ospo@gematik.de
3. Please note: Parts of this code may have been generated using AI-supported technology. Please take this into account, especially when troubleshooting, for security analyses and possible adjustments.

## Contact

If you have ideas or suggestions, feel free to submit a pull request.