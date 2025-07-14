# DFG-Geraetegruppenschluessel / DFG Equipment Group Classification Ontology Extension

 The DFG Gerätegruppenschlüssel Ontology / DFG Equipment Group Classification (DFG GGS) offers an optional ontology extension for classification of instruments. It encodes the [Deutsche Forschungsgemeinschaft Gerätegruppenschlüssel](https://www.dfg.de/de/foerderung/foerdermoeglichkeiten/programme/infrastruktur/wgi/geraetegruppenschluessel) into an OWL RDF-based ontology, where each group at each level of the hierarchy (H - Hundertergruppen, Z - Zehnergruppen, E - Einergruppen) is converted into an owl:Class with subclass statements according to the hierarchy. Labels are provided in German (no English translation at time of making). This exension may be useful to VIVO users looking for a way to classify instruments.

# Ontology Extension

**Main features**

- 4517 classes in total, no properties  
- 3-tier hierarchy  
  - H (highest level) - 10 Classes  
  - Z (middle level) - 94 Classes  
  - E (lowest level) - 4413 Classes  
- Nested under Instrument class (currently http://purl.obolibrary.org/obo/ERO_0000004 which will eventually be replaced)  
- German labels

 - prefix: dfgggs  

[DFG GGS Ontology OWL file](ontology/dfgggs_ontology_extension.owl)  
[DFG GGS Ontology TTL file](ontology/dfgggs_ontology_extension.ttl)

<img src="media/dfgggs protege sample.png" alt="Protege Sample of Ontology" width="500"/>  

Sample of the hierarchy in Protege, showing all ten H-level classes and two Z-level groups. 


# Resources  

How-to use protege to narrow down extension to your use case   
How to import ontology extension into VIVO  
[Deutsche Forschungsgemeinschaft Gerätegruppenschlüssel](https://www.dfg.de/de/foerderung/foerdermoeglichkeiten/programme/infrastruktur/wgi/geraetegruppenschluessel)  
[Geraetegruppenschluessel spreadsheet from DFG](/geraetegruppenschluessel.xlsx)  

# Creating the Ontology Extension  
  
 CSV file, Scripts, workflow, considerations to create OWL/TTL file from spreadsheet 
