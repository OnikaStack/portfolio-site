import zipfile
import os

# Define your HTML and CSS content
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Onika Javu | Portfolio</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Onika Javu</h1>
        <p>Aspiring Full-Stack Developer & Data Enthusiast</p>
    </header>
    <section class="about">
        <h2>About Me</h2>
        <p>I'm Onika Javu, a third-year Computer Science student with a strong foundation in both front-end and back-end development...</p>
    </section>
    <section class="skills">
        <h2>Skills</h2>
        <ul>
            <li><strong>Languages:</strong> HTML, CSS, JavaScript, Python, SQL</li>
            <li><strong>Front-End:</strong> React, Bootstrap, Tailwind CSS</li>
            <li><strong>Back-End:</strong> Node.js, Express.js</li>
            <li><strong>Databases:</strong> MySQL, MongoDB</li>
            <li><strong>Data Science:</strong> Pandas, NumPy, Matplotlib, Jupyter Notebooks</li>
            <li><strong>Tools:</strong> Git, GitHub, VS Code, Postman</li>
        </ul>
    </section>
    <section class="projects">
        <h2>Projects</h2>
        <div class="project"><h3>Student Task Tracker App</h3><p>A full-stack task management tool...</p></div>
        <div class="project"><h3>COVID-19 Data Dashboard</h3><p>An interactive dashboard showing global trends...</p></div>
        <div class="project"><h3>E-Commerce Product Catalog</h3><p>A responsive catalog with filtering...</p></div>
    </section>
    <section class="contact">
        <h2>Contact</h2>
        <p>Email: <a href="mailto:eduv4861489@vossie.net">eduv4861489@vossie.net</a></p>
        <p>GitHub: <a href="https://github.com/OnikaStack">OnikaStack</a></p>
        <p>LinkedIn: <em>Your profile URL</em></p>
    </section>
    <footer>
        <p>&copy; 2025 Onika Javu. All rights reserved.</p>
    </footer>
</body>
</html>
"""

css_content = """body {
    background-color: #121212;
    color: #e0e0e0;
    font-family: 'Segoe UI', sans-serif;
    margin: 0;
}
header, footer {
    background: #1f1f1f;
    text-align: center;
    padding: 2rem 1rem;
}
section {
    padding: 2rem 3rem;
    max-width: 900px;
    margin: auto;
}
h2 {
    color: #fff;
    border-bottom: 2px solid #007BFF;
    padding-bottom: 0.5rem;
}
a {
    color: #66b2ff;
    text-decoration: none;
}
.project {
    background: #1c1c1c;
    padding: 1rem;
    margin-bottom: 1.5rem;
    border-radius: 8px;
}
"""

# Create directory and write files
os.makedirs("onika_portfolio", exist_ok=True)
with open("onika_portfolio/index.html", "w") as f:
    f.write(html_content)
with open("onika_portfolio/style.css", "w") as f:
    f.write(css_content)

# Create zip file
with zipfile.ZipFile("onika_portfolio.zip", 'w') as zipf:
    zipf.write("onika_portfolio/index.html", arcname="index.html")
    zipf.write("onika_portfolio/style.css", arcname="style.css")

print("onika_portfolio.zip has been created.")
