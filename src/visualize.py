import json
import networkx as nx
import plotly.graph_objects as go


def visualize():
    data = load_data()

    G = nx.Graph()
    for user, followers in data.items():
        for follower in followers:
            G.add_edge(user, follower)

    pos = nx.spring_layout(G, k=105, iterations=10000)

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
        line=dict(width=0.5, color="#888"),
        hoverinfo="none",
        mode="lines",
    )

    node_x = []
    node_y = []
    node_customdata = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_customdata.append(f"https://www.instagram.com/{node}")

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=[node for node in G.nodes()],
        customdata=node_customdata,
        hoverinfo="text",
        marker=dict(
            showscale=True,
            colorscale="YlGnBu",
            size=10,
            colorbar=dict(
                thickness=15,
                title="Node Connections",
                xanchor="left",
                titleside="right",
            ),
        ),
    )

    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title="Social Network",
            titlefont_size=16,
            showlegend=False,
            hovermode="closest",
            margin=dict(b=40, l=40, r=40, t=40),
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
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        ),
    )

    fig.write_html("vars/visualization.html")
    fig.write_image("vars/visualization.png", width=1920, height=1080, scale=2)
    fig.show()


def load_data(filename="vars/connections.json"):
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


if __name__ == "__main__":
    visualize()
