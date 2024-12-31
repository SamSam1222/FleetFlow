

# FleetFlow

FleetFlow is a Django-based transport logistics application designed to simplify and streamline logistics operations. With a focus on efficiency and reliability, FleetFlow offers tools to manage routes, vehicles, and logistics services.

---

## Features

- **About Page**: Learn more about FleetFlow's mission and values.
- **Services Page**: Explore the various logistics services offered.
- **Route Management**: Manage and track available transport routes.
- **Customizable Templates**: Easy-to-customize HTML templates for all pages.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/FleetFlow.git
   cd FleetFlow
   ```
### 2. Set Up Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv velvet_aura_env
source env/bin/activate  # On Windows, use FleetFlow\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages:
``` bash
pip install -r requirements.txt
```

### 4. Set Up the Database
Run migrations to set up the database:
``` bash
python manage.py migrate
```


### 5. Create a Superuser
Create a superuser to access the Django admin:
``` bash
python manage.py createsuperuser

```

### 6. Run the Development Server
Start the Django development server:
``` bash
python manage.py runserver
```

### 5. Admin Interface
The admin interface uses the Jazzmin theme for an enhanced user experience. You can manage the FleetFlow's services and bookings by logging in to the admin panel at:
``` bash
http://127.0.0.1:8000/admin/
```

### Project Structure

FleetFlow/
├── FleetFlow/         # Main project folder containing settings and configurations
├── logistics/           # Django app that manages logistics services and routes
│   ├── templates/logistics/   # Contains HTML templates for rendering logistics pages
│   ├── static/logistics/      # Contains static files like CSS and images
│   ├── models.py         # Models for services and routes
│   ├── views.py          # Views for handling requests
├── requirements.txt      # Lists all Python dependencies for the project
├── manage.py             # Entry point for Django commands


### Technologies Used
1. Django: Web framework used for backend development.
2. Python: Programming language.
3. Jazzmin: Admin interface theme for Django.
4. SQLite: Default database used for development (you can switch to PostgreSQL or other databases).


### Customizations
1. The admin interface is customized using the Jazzmin theme.
2. You can customize the FleetFlow services and booking models in the FleetFlow/models.py file.
3. The JAZZMIN_SETTINGS in settings.py can be modified to change the admin interface’s branding.

### Contributing
Feel free to fork the repository and submit pull requests. Contributions are always welcome!


### License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or suggestions, you can reach out via email at samuelemenike4321@gmail.com

