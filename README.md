# socialnetwork

## TL:DR

```console
python main.py --username USERNAME --password PASSWORD
```

<iframe src="vars/visualization.html" width="100%" height="500px"></iframe>

## Dependencies

- instaloader
- networkx
- plotly
- python-dotenv
- requests

```console
pip install instaloader python-dotenv tqdm
```

## Advanced Usage

If you're getting tired of pasting your username and password
every time, create a ```.env``` file in ```vars/```:

```console
src/.env
    USERNAME=your_username
    PASSWORD=your_password
```

## Troubleshooting

### Instagram blocking execution

Open up [Instagram](instagram.com) in your browser. It helps immensely to
have an actual session going at the same time the script is executing.

### ```LoginRequiredException```

The issue is exactly what it says on the box. Log in to get a profile's followers.

### ```BadCredentialsException```

Wrong password or username.
