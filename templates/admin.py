<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <div class="container">
        <h1>Admin Panel</h1>
        <a href="/add">Add New Blog</a>
        <h2>Existing Blogs:</h2>
        <ul>
            {% for blog in blogs %}
            <li>
                <h3>{{ blog.title }}</h3>
                <p>{{ blog.content }}</p>
                <a href="/delete/{{ blog.id }}">Delete</a>
            </li>
            {% endfor %}
        </ul>
        <a href="/logout">Logout</a>
    </div>
</body>
</html>
