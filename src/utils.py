"""
Utility functions for the Delta-Motif tutorial notebooks.

This module contains helper functions for creating graphs.
"""
from typing import List
import os
import gzip
import urllib.request
from pathlib import Path

import rustworkx as rx


def create_example_graph() -> rx.PyGraph:
    """
    Create a small example graph with 5 nodes.
    This graph contains multiple triangles and other patterns.

    Returns:
    --------
    rx.PyGraph
        A graph with 5 nodes and 6 edges containing 2 triangles
    """
    graph = rx.PyGraph()

    # Add 5 nodes
    nodes = [graph.add_node(i) for i in range(5)]

    # Add edges to create an interesting structure
    # This creates multiple triangles: (0,1,2), (2,3,4)
    edges = [
        (0, 1), (1, 2), (2, 0),  # Triangle 1
        (2, 3), (3, 4), (4, 2),  # Triangle 2
    ]

    for src, dst in edges:
        graph.add_edge(src, dst, None)

    return graph

def gen_edge_colors(graph: rx.PyGraph, highlight_nodes: List[int]) -> List[str]:
    edge_colors = []
    highlight_set = set(highlight_nodes)
    for src, dst in graph.edge_list():
        if src in highlight_set and dst in highlight_set:
            edge_colors.append('red')
        else:
            edge_colors.append('gray')
    return edge_colors


def load_facebook_dataset(cache_dir: str = "./data") -> rx.PyGraph:
    """
    Download and load the Facebook social network dataset from SNAP.

    Dataset: Facebook combined ego-networks
    - Nodes: 4,039 (anonymized Facebook users)
    - Edges: 88,234 (friendships)
    - Source: https://snap.stanford.edu/data/ego-Facebook.html

    The dataset is cached locally after first download.

    Parameters:
    -----------
    cache_dir : str
        Directory to cache the downloaded dataset (default: "./data")

    Returns:
    --------
    rx.PyGraph
        Undirected graph with Facebook social network
    """
    # Create cache directory if it doesn't exist
    cache_path = Path(cache_dir)
    cache_path.mkdir(exist_ok=True)

    # File paths
    dataset_url = "https://snap.stanford.edu/data/facebook_combined.txt.gz"
    gz_filepath = cache_path / "facebook_combined.txt.gz"
    txt_filepath = cache_path / "facebook_combined.txt"

    # Download if not cached
    if not txt_filepath.exists():
        print(f"📥 Downloading Facebook dataset from SNAP...")

        if not gz_filepath.exists():
            urllib.request.urlretrieve(dataset_url, gz_filepath)
            print(f"✅ Downloaded to {gz_filepath}")

        # Decompress
        print(f"📦 Decompressing...")
        with gzip.open(gz_filepath, 'rb') as f_in:
            with open(txt_filepath, 'wb') as f_out:
                f_out.write(f_in.read())
        print(f"✅ Extracted to {txt_filepath}")
    else:
        print(f"✅ Using cached dataset at {txt_filepath}")

    # Load into rustworkx graph
    print(f"📊 Loading graph...")
    graph = rx.PyGraph()
    node_map = {}

    with open(txt_filepath, 'r') as f:
        for line in f:
            if line.startswith('#'):  # Skip comments
                continue

            parts = line.strip().split()
            if len(parts) != 2:
                continue

            src, dst = parts

            # Add nodes if they don't exist
            if src not in node_map:
                node_map[src] = graph.add_node(int(src))
            if dst not in node_map:
                node_map[dst] = graph.add_node(int(dst))

            # Add edge
            graph.add_edge(node_map[src], node_map[dst], None)

    print(f"✅ Loaded graph: {graph.num_nodes()} nodes, {graph.num_edges()} edges")
    return graph
