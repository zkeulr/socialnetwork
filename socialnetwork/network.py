import networkx as nx
import plotly.express as px
import plotly.graph_objects as go
from scipy.spatial import ConvexHull
import numpy as np

try:
    from . import utils
except ImportError:
    import utils

text_size = 10


def network(seed=0, k=100):
    data = utils.load_connections()

    G = nx.Graph()
    for user, followers in data.items():
        for follower in followers:
            G.add_edge(user, follower)

    connected_components = list(nx.connected_components(G))
    cluster_colors = px.colors.qualitative.Plotly
    node_colors = {}
    for i, component in enumerate(connected_components):
        for node in component:
            node_colors[node] = cluster_colors[i % len(cluster_colors)]


    pos = {}
    offset = np.array([0.0, 0.0])
    grid_size = int(np.ceil(np.sqrt(len(connected_components))))
    spacing = 1.0

    for idx, component in enumerate(connected_components):
        subgraph = G.subgraph(component)
        sub_pos = nx.spring_layout(subgraph, k=k, iterations=10000, seed=seed)
        
        min_x = min(pos[0] for pos in sub_pos.values())
        min_y = min(pos[1] for pos in sub_pos.values())
        max_x = max(pos[0] for pos in sub_pos.values())
        max_y = max(pos[1] for pos in sub_pos.values())
        
        row = idx // grid_size
        col = idx % grid_size
        offset = np.array([col * (max_x - min_x + spacing), row * (max_y - min_y + spacing)], dtype=np.float64)
        
        for node in sub_pos:
            sub_pos[node] += offset
        
        pos.update(sub_pos)

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
            size=5,
            color=node_color,
            colorbar=dict(
                thickness=15,
                title="Node Connections",
                xanchor="left",
                titleside="right",
            ),
        ),
        textfont=dict(size=text_size),
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

    for i, component in enumerate(connected_components):
        nodes = list(component)
        points = np.array([pos[node] for node in nodes])

        if len(points) > 2:
            hull = ConvexHull(points)
            hull_points = points[hull.vertices]
            hull_points = np.append(hull_points, [hull_points[0]], axis=0)

            fig.add_trace(
                go.Scatter(
                    x=hull_points[:, 0],
                    y=hull_points[:, 1],
                    fill="toself",
                    fillcolor=cluster_colors[i % len(cluster_colors)],
                    opacity=0.1,
                    line=dict(color=cluster_colors[i % len(cluster_colors)]),
                    hoverinfo="none",
                    mode="lines",
                )
            )

    utils.save(fig, "network")
    fig.show()


if __name__ == "__main__":
    network()
