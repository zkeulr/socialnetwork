# socialnetwork

## TL:DR

```console
python main.py --username USERNAME --password PASSWORD
```

## Dependencies

- instaloader
- python-dotenv
- requests
- tqdm

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

### ```LoginRequiredException```

The issue is exactly what it says on the box. Log in to get a profile's followers.

### ```BadCredentialsException```

Wrong password or username.
