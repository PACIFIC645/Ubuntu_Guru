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

2. **Install dependencies:**
   Install the necessary Python packages specified in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

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
