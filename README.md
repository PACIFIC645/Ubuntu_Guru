# Ubuntu Guru

Ubuntu Guru is a Django-based web platform designed to foster interactive political engagement. It features a robust poll system that allows users to vote on various topics, track global election trends, and engage with political content interactively.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

### Prerequisites
Ensure you have Python and Django installed on your system. If not, you can download Python from [python.org](https://python.org) and Django via pip:
```bash
pip install Django
```

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/PACIFIC645/Ubuntu_Guru.git
   cd Ubuntu_Guru
   ```

### 2. Install Dependencies

To install the necessary Python packages specified in the `requirements.txt` file, execute the following command in your terminal. This will install all the dependencies required for the project to run:

```bash
pip install -r requirements.txt
```

**Important Notes:**
- **Python Version Compatibility:** On some systems, especially where both Python 2 and Python 3 are installed, you may need to use `pip3` instead of `pip` to ensure that the packages are installed for Python 3.
  
  ```bash
  pip3 install -r requirements.txt
  ```

- **Local Environment:** The `-l` flag in the pip command refers to installing the packages locally. If you're using a virtual environment (recommended), all packages will be installed in this environment, avoiding global installation and potential conflicts:
  
  ```bash
  pip install -r requirements.txt -l
  ```

- **Cleaning Up `requirements.txt`:** The `requirements.txt` file might include some unnecessary or system-specific packages (like `pywin32` for Windows). It's a good practice to review and clean up the `requirements.txt` file periodically, removing any packages not directly needed by the project.

3. **Set up the database:**
   Run the following commands to prepare your database.
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the server:**
   Start the Django development server.
   ```bash
   python manage.py runserver
   ```

## Setting Up and Running with Virtual Environment

To run Ubuntu_Guru locally using a virtual environment, follow these steps:

1. **Clone the repository**:
   ```
   git clone https://github.com/PACIFIC645/Ubuntu_Guru.git
   cd Ubuntu_Guru
   ```

2. **Set up a virtual environment**:
   If you don't have `virtualenv` installed, you can install it using pip:
   ```
   pip install virtualenv
   ```
   Create and activate the virtual environment:
   ```
   virtualenv venv
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   This step ensures your database schema is up to date with the models defined.
   ```
   python manage.py migrate
   ```

5. **Start the development server**:
   ```
   python manage.py runserver
   ```
   This will start the local server, allowing you to access Ubuntu_Guru at `http://127.0.0.1:8000/`.

## Running with Docker

To run Ubuntu_Guru using Docker, ensure you have Docker installed on your machine. Then follow these steps:

1. **Build the Docker image**:
   Navigate to the directory containing your project and Dockerfile, then build your Docker image:
   ```
   docker build -t ubuntu_guru_app .
   ```

2. **Run the container**:
   ```
   docker run -p 8000:8000 ubuntu_guru_app
   ```
   This command runs your application inside a Docker container and makes it accessible at `http://localhost:8000`.


## Usage
After installation, the site is accessible at `http://127.0.0.1:8000/`. You can:
- **Register and Login:** Secure user authentication to participate in polls.
- **View and Participate in Polls:** Engage with various polls and see real-time results.
- **Track Election Trends:** Follow the "Poll Tracker" section for latest updates on global elections.

### Screenshots
- **About Us Page:** ![About Us Ubuntu Guru](https://imgur.com/nSEIepe.jpg)
- **View Polls and Social Media Links:** ![View Polls](https://imgur.com/1krnlwi.jpg) 
- **Poll Tracker Section:** ![Poll Tracker](https://imgur.com/kRajCzq.jpg)

## Features
- **Dynamic Poll System:** Allows users to vote and see results on various political topics.
- **User Authentication:** Manages user registration and login securely.
- **Responsive Design:** Ensures the website is accessible on all devices.

## Requirements
This project uses several key technologies:
- Django 3.2.6
- django-crispy-forms 1.12.0
- Bootstrap for styling

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
- **Email:** stqpictures@gmail.com
- **LinkedIn:** [My LinkedIn](https://linkedin.com/in/mafekefekeng)
- **GitHub:** [My GitHub](https://github.com/PACIFIC645)


