# switchtube-downloader

## Disclaimer

**This software is intended strictly for **educational, legal, and personal use** only.**

The authors and contributors of this project **do not support, condone, or endorse any illegal use** of this software. By using this software, you agree to the following:

1. You are solely responsible for complying with all applicable copyright laws and terms of service for the content you download or interact with.
2. This software should **not be used** to download, distribute, or access **copyright-protected, restricted, or proprietary content** without explicit permission from the content owner or provider.
3. This project and its contributors are not liable for any misuse, and **no guarantees** are provided regarding functionality or legal compliance.

Please use this tool responsibly and ensure that any downloads comply with relevant terms of service and copyright laws.

---

**NOTE**: If you are uncertain about the legality of downloading specific content, please **consult the terms of service** for that content or seek legal advice.

---

## Installation

### Step 1: Set up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies for this project. To set up a virtual environment, follow these steps:

1. **Create a virtual environment** by running the following command:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. For more detailed guidance on virtual environments, refer to the [official Python documentation](https://docs.python.org/3/library/venv.html).

### Step 2: Install Requirements

With the virtual environment activated, install the required packages:
```bash
pip install -r requirements.txt
```

This will install all necessary dependencies listed in the `requirements.txt` file.

---

## Configuration

This project requires certain environment variables to be set up in a `.env` file to function correctly. Create a `.env` file in the root directory of the project and include the following information:

```plaintext
SCHOOL=your_school_name
USERNAME=your_username
PASSWORD=your_password
```
Ensure that your `.env` file is securely stored and not shared publicly. You may want to add `.env` to your `.gitignore` file to prevent it from being committed to version control.

---

