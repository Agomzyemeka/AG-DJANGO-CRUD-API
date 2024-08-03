# AG Django CRUD API

![AG Django CRUD API](https://media.giphy.com/media/l0HlPjez3pOsuP6uc/giphy.gif)  <!-- Replace with an actual link to your GIF -->

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

The project is deployed on Render. You can access the deployed API at [https://ag-django-crud-api.onrender.com](https://ag-django-crud-api.onrender.com).

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

## Contributing

Feel free to submit pull requests and open issues to contribute to this project.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Render](https://render.com/)
