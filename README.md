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

2. **Install Dependencies**
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

3. **Set up the database:**
   Before you can start using the application, you need to set up the database by creating the necessary tables. Run the following commands to make migrations and migrate the database. This step initializes your database schema according to the Django models defined in your application.
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the server:**
   Start the Django development server to serve your application locally.
   ```bash
   python manage.py runserver
   ```

## Setting Up and Running with Virtual Environment

To run Ubuntu Guru locally using a virtual environment, follow these steps:

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
   This will start the local server, allowing you to access Ubuntu Guru at `http://127.0.0.1:8000/`.


## Running with Docker

Running Ubuntu Guru with Docker simplifies setup and ensures consistency across different environments. Below are instructions for both building the image locally and pulling a pre-built image from Docker Hub.

### Building and Running Locally

1. **Build the Docker image**:
   Navigate to the directory containing your project and Dockerfile. Build the Docker image using the command:
   ```
   docker build -t ubuntu_guru_current .
   ```

2. **Run the container**:
   Run your Docker container using the command below, which makes your application accessible at `http://localhost:8000`:
   ```
   docker run -p 8000:8000 ubuntu_guru_current
   ```

### Pulling and Running from Docker Hub

Alternatively, if you prefer using a pre-built image hosted on Docker Hub, follow these steps:

1. **Pull the Docker image**:
   Replace `latest` with the appropriate version tag if necessary. Pull the image using:
   ```
   docker pull pacic645/ubuntu_guru_current:latest
   ```

2. **Run the container**:
   Start your Docker container with the following command, which also exposes the application at `http://localhost:8000`:
   ```
   docker run -p 8000:8000 pacic645/ubuntu_guru_current:latest
   ```


### Database Setup

Before you start the application, ensure the database is properly set up:

- **Database Migrations**:
  If your Docker setup doesn't handle migrations automatically, you may need to execute migrations manually. After the container is running, follow these steps to perform migrations:

  1. **Find the Container ID**:
     Run `docker ps` to list all running containers. The output will show the container ID which you will need for the next steps.
     ```bash
     docker ps
     ```
     Example output:
     ```
     CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS         PORTS                    NAMES
     1fa3f2d4af9d   pacic645/ubuntu_guru_current "docker-entrypoint.s…"   10 minutes ago  Up 10 minutes  0.0.0.0:8000->8000/tcp   mystified_turing
     ```

  2. **Run Migrations**:
     Using the CONTAINER ID from the `docker ps` output, replace `CONTAINER_ID` in the commands below:
     ```bash
     docker exec -it CONTAINER_ID python manage.py makemigrations
     docker exec -it CONTAINER_ID python manage.py migrate
     ```

     Replace `CONTAINER_ID` with the actual ID of your running container, such as `1fa3f2d4af9d` from the example above.


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

