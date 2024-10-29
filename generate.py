import os

def gen_index_page(mens_folder, womens_folder, outfile='index.html'):
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Athlete Stats Homepage</title>
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h1>Welcome to Athlete Stats</h1>
        <p>Select a team to view athlete details and performance stats.</p>
    </header>

    <main>
        <section>
            <h2>Men's Team</h2>
            <ul>
    '''
    # List all HTML files in men's team folder
    mens_files = [f for f in os.listdir(mens_folder) if f.endswith('.html')]
    for file in mens_files:
        athlete_name = file.replace(".html", "")
        html_content += f'<li><a href="mens_team/{file}">{athlete_name}</a></li>\n'

    html_content += '''
            </ul>
        </section>

        <section>
            <h2>Women's Team</h2>
            <ul>
    '''
    # List all HTML files in women's team folder
    womens_files = [f for f in os.listdir(womens_folder) if f.endswith('.html')]
    for file in womens_files:
        athlete_name = file.replace(".html", "")
        html_content += f'<li><a href="womens_team/{file}">{athlete_name}</a></li>\n'

    html_content += '''
            </ul>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Skyline High School</p>
    </footer>
</body>
</html>
    '''
    
    # Write the generated HTML to index.html
    with open(outfile, 'w') as f:
        f.write(html_content)

# Define the folder paths
gen_index_page('mens_team', 'womens_team')
