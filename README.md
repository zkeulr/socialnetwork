# socialnetwork

## TL:DR

```console
python main.py --username USERNAME --password PASSWORD
```

Generates a dynamic visualization of Instagram connections, like so.

![Instagram network](vars/visualization.png)

## Dependencies

- [instaloader](https://github.com/instaloader/instaloader)
- networkx
- plotly
- python-dotenv

```console
pip install instaloader networkx plotly python-dotenv 
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
