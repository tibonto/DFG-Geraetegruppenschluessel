from lxml import etree
from datetime import datetime
import glob
import os

def convert_rdf_description_to_owl_class(xml_path_in, xml_path_out):
    parser = etree.XMLParser(ns_clean=True, remove_blank_text=True)
    tree = etree.parse(xml_path_in, parser)
    root = tree.getroot()

    RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    OWL_NS = "http://www.w3.org/2002/07/owl#"

    rdf = "{%s}" % RDF_NS
    owl = "{%s}" % OWL_NS

    for desc in root.findall(f".//{rdf}Description"):
        # Check if rdf:type child exists with owl:Class resource
        types = desc.findall(f"{rdf}type")
        for t in types:
            if t.get(f"{rdf}resource") == OWL_NS + "Class":
                # Change tag to owl:Class
                desc.tag = owl + "Class"
                # Remove rdf:type child (optional)
                desc.remove(t)
                break

    tree.write(xml_path_out, pretty_print=True, xml_declaration=True, encoding="utf-8")

# Find the latest timestamped dfgggs*.owl file in the current directory, output of create_ggs_ontology.py
owl_files = glob.glob("dfgggs*.owl")
if not owl_files:
    raise FileNotFoundError("No input OWL file matching 'dfgggs*.owl' found.")
latest_owl = max(owl_files, key=os.path.getctime)

timestamp = datetime.now().strftime("%Y%m%d_%H%M")
output_file = f"dfgggs_postprocessed_{timestamp}.owl"

convert_rdf_description_to_owl_class(latest_owl, output_file)
