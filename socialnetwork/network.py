import networkx as nx
import plotly.graph_objects as go
from socialnetwork import utils


def network(seed=0, k=100):
    data = utils.load_connections()

    G = nx.Graph()
    for user, followers in data.items():
        for follower in followers:
            G.add_edge(user, follower)

    pos = nx.spring_layout(G, k=k, iterations=10000, seed=seed)

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=0.3, color="#888"),
        hoverinfo="none",
        mode="lines",
    )

    node_x = []
    node_y = []
    node_customdata = []
    hover_text = []
    node_color = []

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_color.append(G.degree[node])

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=[
            f'<a href="https://www.instagram.com/{node}" target="_blank">{node}</a>'
            for node in G.nodes()
        ],
        customdata=node_customdata,
        hoverinfo="text",
        hovertext=hover_text,
        marker=dict(
            showscale=True,
            colorscale="Viridis",
            size=10,
            color=node_color,
            colorbar=dict(
                thickness=15,
                title="Node Connections",
                xanchor="left",
                titleside="right",
            ),
        ),
        textfont=dict(size=10),
    )

    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title="Social Network",
            titlefont_size=32,
            showlegend=False,
            hovermode="closest",
            margin=dict(b=40, l=40, r=40, t=80),
            annotations=[
                dict(
                    text="Click on a node to visit profile",
                    showarrow=False,
                    xref="paper",
                    yref="paper",
                    x=0.005,
                    y=0.002,
                )
            ],
            xaxis=dict(
                showgrid=False, zeroline=False, showticklabels=False, showline=False
            ),
            yaxis=dict(
                showgrid=False, zeroline=False, showticklabels=False, showline=False
            ),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        ),
    )

    utils.save(fig, "network")
    fig.show()


if __name__ == "__main__":
    network()
