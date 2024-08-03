# socialnetwork

## TL;DR

```console
python main.py --username USERNAME --password PASSWORD --seed SEED
```

Generates a dynamic analysis of Instagram connections.

![Network](output/network.png)
![Clusters](output/cluster.png)

To interact with your network, open [```output/network.html```](output/network.html)
and [```output/cluster.html```](output/cluster.html) in your broswer.

## Dependencies

- [instaloader](https://github.com/instaloader/instaloader)
- [kaleido](https://github.com/plotly/Kaleido)
- [networkx](https://github.com/networkx/networkx)
- [pandas](https://github.com/pandas-dev/pandas)
- [plotly](https://github.com/plotly/plotly.py)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

```console
pip install instaloader kaleido networkx pandas plotly python-dotenv 
```

## Advanced Usage

If you're getting tired of entering your username and password, create a ```.env``` file.

```console
.env
    USERNAME=your_username
    PASSWORD=your_password
    SEED=arbitrary_integer
    K=value_for_neat_graph
```

## Troubleshooting

### Instagram blocking execution

Open up [Instagram](https://instagram.com) in your browser. It helps immensely to
have an actual session going at the same time the script is executing.

### ```LoginRequiredException```

The issue is exactly what it says on the box. Log in to get a profile's followers.

### ```BadCredentialsException```

Wrong password or username.
