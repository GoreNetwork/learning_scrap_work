from py2cytoscape.data.cyrest_client import CyRestClient

# Initialize client to connect to a running Cytoscape instance
cy = CyRestClient()

# Create a basic network
network = cy.network.create(name="My Network")

# Add nodes
cy.network.add_nodes(network, ["A", "B", "C"])

# Add edges
cy.network.add_edges(network, source=["A", "B"], target=["B", "C"])

# Apply layout and style
cy.layout.apply(network, "force-directed")
cy.style.apply(style_name="default", network=network)

# Show in Cytoscape
cy.session.save()
