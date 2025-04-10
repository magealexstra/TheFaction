<div align="center">
  <h1>🔱 TheFaction</h1>
  <p><i>A modern Django portfolio website for showcasing projects, skills, and information resources.</i></p>
  
  <p>
    <a href="#features">Features</a> •
    <a href="#installation">Installation</a> •
    <a href="#security">Security</a> •
    <a href="#project-structure">Structure</a> •
    <a href="#usage">Usage</a> •
    <a href="#technologies">Technologies</a> •
    <a href="#deployment">Deployment</a>
  </p>
  
  <p>
    <img src="https://img.shields.io/badge/Django-5.2-green.svg" alt="Django 5.2">
    <img src="https://img.shields.io/badge/Python-3.12-blue.svg" alt="Python 3.12">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </p>
</div>

---

## ✨ Features <a name="features"></a>

- 📂 **Project portfolio** with categories and filtering
- 🖼️ **Image gallery support** for each project
- 🔄 **GitHub repository integration**
- 💻 **Technology showcase**
- 📚 **Information resources section**
- 📱 **Responsive design** for all devices
- 🔐 **Admin dashboard** for content management
- 🛡️ **Secure configuration** management

## 🚀 Installation <a name="installation"></a>

1. **Clone the repository:**
   ```bash
   git clone https://github.com/magealexstra/TheFaction.git
   cd TheFaction
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up configuration:**
   ```bash
   # Create a secrets.py file from the template
   cp thefaction/secrets_template.py thefaction/secrets.py
   
   # Edit the file with your secure settings
   nano thefaction/secrets.py  # or use your preferred editor
   ```

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the site at** [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🔒 Security <a name="security"></a>

The project uses a `secrets.py` file (ignored by Git) to store sensitive configuration:

| Setting Type | Description |
|--------------|-------------|
| 🔑 Django Secret Key | Used for cryptographic signing |
| 🗄️ Database Credentials | Username, password, host information |
| 📧 Email Settings | SMTP server details |
| 🔐 API Keys | GitHub and other external services |

> ⚠️ **Never commit your `secrets.py` file to version control!** The repository includes a template (`secrets_template.py`) that you should copy and customize with your own values.

## 📁 Project Structure <a name="project-structure"></a>

```
TheFaction/
│
├── portfolio/                  # Main app
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── github_utils.py         # GitHub API utilities
│   ├── templates/              # HTML templates
│   └── static/                 # CSS, JS, and static files
│
├── thefaction/                 # Project configuration
│   ├── settings.py             # Django settings
│   ├── secrets.py              # Sensitive configuration (not in repo)
│   ├── secrets_template.py     # Template for secrets.py
│   └── urls.py                 # URL routing
│
├── requirements.txt            # Project dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

## 📝 Usage <a name="usage"></a>

- **🔐 Admin Panel:**
  - Access at `/admin/` to manage content
  - Login with superuser credentials

- **👨‍💻 Content Management:**
  - Add technologies, projects, and information resources
  - Upload images for projects
  - Link to GitHub repositories for code-based projects

## 🛠️ Technologies <a name="technologies"></a>

<p>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** SQLite (development), PostgreSQL (production)
- **API Integration:** GitHub API

## 🌐 Deployment <a name="deployment"></a>

For production deployment:

1. **Set up a PostgreSQL database**
2. **Configure all sensitive settings in `secrets.py`**
3. **Set `DEBUG = False` in production**
4. **Use a production WSGI server** (e.g., Gunicorn)
5. **Configure static files serving** (e.g., Whitenoise or a reverse proxy)

---

<div align="center">
  <p>Created with ❤️ by <a href="https://github.com/magealexstra">magealexstra</a></p>
</div>