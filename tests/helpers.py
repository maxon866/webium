import os


current_dir_path = os.path.dirname(__file__)
html_dir_path = os.path.join(current_dir_path, 'pages')


def get_url(suffix=""):
    path = os.path.join(html_dir_path, suffix)
    return 'file://' + path
