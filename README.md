# Public Key Bit Sorter 🔑

![GitHub release](https://img.shields.io/github/release/Hipa319/public_key_bit_sorter.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Overview

Welcome to the **Public Key Bit Sorter** repository! This project focuses on bit-level entropy analysis of uncompressed public keys. It serves as a valuable tool for researchers and auditors in the fields of cryptography and blockchain analysis. By examining the entropy of public keys, users can gain insights into their randomness and security.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Bit-level Analysis**: Perform detailed analysis of public keys to assess their entropy.
- **Multiprocessing Support**: Utilize multiple cores for faster processing.
- **Command Line Interface**: Easy to use CLI for seamless integration into your workflow.
- **Progress Tracking**: Visual feedback on processing with the `tqdm` library.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Installation

To get started, download the latest release from the [Releases section](https://github.com/Hipa319/public_key_bit_sorter/releases). Follow these steps to install:

1. Download the release file.
2. Extract the contents.
3. Open your terminal or command prompt.
4. Navigate to the extracted folder.
5. Run the following command to install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Once you have installed the Public Key Bit Sorter, you can use it directly from the command line. Here’s a simple command to analyze a public key:

```bash
python bit_sorter.py <path_to_public_key_file>
```

### Example

If you have a public key file named `public_key.txt`, you would run:

```bash
python bit_sorter.py public_key.txt
```

The tool will process the file and provide an analysis of the entropy.

## How It Works

The Public Key Bit Sorter operates by reading uncompressed public keys and calculating their bit-level entropy. Here's a brief overview of the process:

1. **Input**: The user provides a file containing public keys.
2. **Bit Extraction**: The program extracts the bits from each key.
3. **Entropy Calculation**: It calculates the entropy of the bits using statistical methods.
4. **Output**: The results are displayed in the terminal, showing the entropy score and other relevant metrics.

### Entropy Explained

Entropy is a measure of randomness. In the context of cryptography, high entropy indicates that a key is less predictable and therefore more secure. The Public Key Bit Sorter provides a numerical value representing the entropy of each public key analyzed.

## Contributing

We welcome contributions to improve the Public Key Bit Sorter. If you want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your branch to your forked repository.
5. Create a pull request.

Please ensure that your code adheres to the project's coding standards and that you have tested your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, feel free to reach out:

- GitHub: [Hipa319](https://github.com/Hipa319)
- Email: hipa319@example.com

Thank you for your interest in the Public Key Bit Sorter! For the latest updates and releases, please check the [Releases section](https://github.com/Hipa319/public_key_bit_sorter/releases).