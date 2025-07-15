import csv
import re
from pathlib import Path
from typing import Tuple
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, OWL, RDFS, SKOS
from datetime import datetime

# Creates the dfgggs ontology (.owl and .ttl) by parsing a CSV version of the DFG Gerätegruppenschlüssel at  
# https://www.dfg.de/de/foerderung/foerdermoeglichkeiten/programme/infrastruktur/wgi/geraetegruppenschluessel

# Each Group is an owl:Class with:
# * URI with namespace https://w3id.org/dfgggs/2025#, based on pattern used for dfgfo 
# * labels in DE. DFG has no English translation of this. 
# * class hierarchy accordinng to DFG Equipment Classification hierarchy (hundert, zehner, einer)
# * parent class as owl:Thing if no parent is given, else as owl:Class with full URI
# * requires post-processing to convert rdf:Description nodes to owl:Class nodes, to match VIVO owl structure
#          (although it should work as well to use the rdf:Description node structure)


timestamp = datetime.now().strftime("%Y%m%d_%H%M")

# Input files in same folder as the script
base_path = Path(r'C:YOUR PATH HERE')

dfg_onto_metadata_fn = base_path / 'metadata.ttl'
dfg_onto_handles_fn = base_path / 'handles.ttl'
dfg_onto_fn = base_path / f'dfgggs_{timestamp}.ttl'
dfg_onto_fn_owl = base_path / f'dfgggs_{timestamp}.owl'
dfg_csv_en = base_path / 'dfg_instruments_hierarchy.csv'

g_metadata = Graph()
g_metadata.parse(str(dfg_onto_metadata_fn.absolute()))

g_handles = Graph()
g_handles.parse(str(dfg_onto_handles_fn.absolute()))

g_classes = Graph()
ns_str = 'https://w3id.org/dfgggs/2025#'  # Base URI for the DFG GGS ontology
namespace = Namespace(ns_str)

g_classes.namespace_manager.bind('owl', OWL, override=False)
g_classes.namespace_manager.bind('dfgggs', ns_str, override=False)


def create_class(graph, ns, node_name, labels, parent):
    uri_str = f'{ns_str}{node_name}'
    node = URIRef(uri_str)
    print(f'Class: {uri_str} labels: {labels}')

    # type
    graph.add((node, RDF.type, OWL.Class))

    # subClassOf logic: use parent as full URI if it looks like one, else prepend base
    if not parent or parent.lower() == "none":
        graph.add((node, RDFS.subClassOf, OWL.Thing))
    else:
        if parent.startswith("http://") or parent.startswith("https://"):
            parent_uri_str = parent
        else:
            parent_uri_str = f'{ns_str}{parent}'
        parent_node = URIRef(parent_uri_str)
        graph.add((node, RDFS.subClassOf, parent_node))

    # label (German)
    graph.add((node, RDFS.label, Literal(labels[0], lang='de')))

    # Add rdfs:comment with the class ID as string and xsd:string datatype
    graph.add((node, RDFS.comment, Literal(node_name, datatype="http://www.w3.org/2001/XMLSchema#string")))

    # Optionally, add other mappings or labels here
    # graph.add((node, SKOS.prefLabel, Literal(f'{labels[1]}', lang='de')))
    # graph.add((node, SKOS.closeMatch, URIRef(f'http://uri.gbv.de/terminology/dfg2024/{node_name}')))



with open(dfg_csv_en, newline='', encoding="utf-8") as csvfile:
    csvfile = csv.DictReader(csvfile, delimiter=',')
    for row in csvfile:
        # Example: adjust these keys to match your CSV headers
        cell_id = row['ID']
        cell_label = row['Label']
        parent_id = row['ParentID'] if 'ParentID' in row else "http://purl.obolibrary.org/obo/ERO_0000004"

        # Skip rows with 'auto-added' in the label (case-insensitive)
        if 'auto-added' in cell_label.lower():
            continue

        # print(f'CELL ID: <<<<{cell_id}>>>')
        # print(f'Cleaned ID: {cell_id} | Parent: {parent_id}')
        # print(f'CURRENT: {cell_id} - {cell_label}')
        # print(f'PARENT: <<<{parent_id}>>>')

        create_class(
            graph=g_classes,
            ns=namespace,
            node_name=cell_id,
            labels=[cell_label],
            parent=parent_id
        )


# join g_metadata + g_classes graphs into g_joint
g_joint = Graph() # after the g_classes
g_joint = g_metadata + g_classes + g_handles

#print('\n\nSERIALIZE\n\n')
#print(g_joint.serialize())

#save in turte format
g_joint.serialize(destination=dfg_onto_fn, encoding="utf-8", format="turtle")

# save in owl format
g_joint.serialize(destination=dfg_onto_fn_owl, encoding="utf-8", format="xml")

