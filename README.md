# AG Django CRUD API

![Django API](https://camo.githubusercontent.com/4012ae090f03c154db8bb403d3f18ed69667e08b65081ef394deca8c264b6398/68747470733a2f2f6d61786d6175746e65722e636f6d2f7075626c69632f696d616765732f646a616e676f2e676966) <!-- Replace with an actual link to your GIF -->

A simple CRUD (Create, Read, Update, Delete) API built with Django, showcasing the basic functionalities for managing blog posts.

## Features

- Create, read, update, and delete blog posts.
- RESTful API design.
- Deployed on Render.

## Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Django
- PostgreSQL

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables:**

    Create a `.env` file in the root directory and add your environment variables:

    ```env
    DJANGO_SECRET_KEY=your-secret-key
    DB_NAME=your-database-name
    DB_USER=your-database-user
    DB_PASSWORD=your-database-password
    DB_HOST=your-database-host
    DB_PORT=your-database-port
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

## Usage

### Endpoints

- `GET /blogposts/` - Retrieve a list of blog posts.
- `POST /blogposts/` - Create a new blog post.
- `GET /blogposts/<id>/` - Retrieve a single blog post by ID.
- `PUT /blogposts/<id>/` - Update a blog post by ID.
- `DELETE /blogposts/<id>/` - Delete a blog post by ID.

### Example Requests

#### Create a blog post

```bash
curl -X POST http://127.0.0.1:8000/blogposts/ \
-H "Content-Type: application/json" \
-d '{"title": "New Blog Post", "content": "This is the content of the new blog post."}'
```

**Get a list of blog posts**

    ```bash
    curl -X GET http://127.0.0.1:8000/blogposts/
    ```

    ## Deployment

The project is deployed on Render. You can access the deployed API at [https://ag-django-crud-api.onrender.com](https://ag-django-crud-api.onrender.com/blogposts/).

To deploy your own version, follow these steps:

1. **Create a new service on Render and connect your GitHub repository.**
    
2. **Set up the environment variables on Render:**
    
    - DJANGO_SECRET_KEY
    - DB_NAME
    - DB_USER
    - DB_PASSWORD
    - DB_HOST
    - DB_PORT

3. **Trigger a deployment on Render.**

## API Documentation

### Swagger Integration

This project uses Swagger to provide interactive API documentation.

### Setup

1. **Install the Required Packages**:
    
    Make sure you have `drf-yasg` installed. You can add it to your `requirements.txt` or install it directly:
    
    ```bash
    pip install drf-yasg
    ```
    
2. **Update `settings.py`**:
    
    Add `'drf_yasg'` to your `INSTALLED_APPS`:
    
    ```python
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'drf_yasg',
        ...
    ]
    ```
    
3. **Configure URLs**:
    
    In your project's `urls.py`, add the Swagger and Redoc views:
    
    ```python
    from django.contrib import admin
    from django.urls import path, re_path
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="My API",
            default_version='v1',
            description="Test description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@local.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns = [
        path('admin/', admin.site.urls),
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
    ```
    
4. **Access the Documentation**:
    
    Once you have the server running, you can access the Swagger UI at:
    
    ```perl
    http://<your-domain>/swagger/
    ```
    
    And the ReDoc UI at:
    
    ```perl
    http://<your-domain>/redoc/
    ```

### Best Practices

- **Versioning**: Ensure your API versions are properly documented.
- **Security**: Secure your Swagger documentation in production. You might want to restrict access to the Swagger UI or disable it entirely in a production environment.
- **Custom Documentation**: Use the `description` field in your API views and serializers to provide detailed documentation for each endpoint and field.

### Example Screenshot

### Deployment Notes

Ensure that your deployment environment has the necessary configurations for serving static files and that all URL patterns are correctly mapped.

For more detailed instructions, you can refer to the [drf-yasg documentation](https://drf-yasg.readthedocs.io/en/stable/).

## Deployment

### Render.com Configuration

To deploy this project on Render.com, follow these steps:

1. **Create a `render.yaml` file** in the root of your project with the following content:
    
    ```yaml
    services:
      - type: web
        name: myRESTsite
        env: python
        plan: starter
        buildCommand: 
          - pip install -r requirements.txt
          - python manage.py collectstatic --noinput
        startCommand: gunicorn myRESTsite.wsgi --log-file -
        envVars:
          - key: DEBUG
            value: 'False'
          - key: ALLOWED_HOSTS
            value: 'your-app-name.onrender.com'
    ```
    
2. **Deploy your project** by following the instructions on Render.com to link your GitHub repository and start the deployment.
    
3. **Add the collect static command** in the Render.com dashboard under the settings for your web service. Append the following to the build command:
    
    ```bash
    && python manage.py collectstatic --noinput && python manage.py migrate
    ```


## Contributing

Feel free to submit pull requests and open issues to contribute to this project.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Render](https://render.com/)
