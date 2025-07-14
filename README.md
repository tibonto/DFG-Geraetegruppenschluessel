# DFG-Geraetegruppenschluessel / DFG Equipment Group Classification Ontology Extension

 The DFG Gerätegruppenschlüssel Ontology / DFG Equipment Group Classification (DFGGGS) offers an optional ontology extension for classification of instruments. It encodes the [Deutsche Forschungsgemeinschaft Gerätegruppenschlüssel](https://www.dfg.de/de/foerderung/foerdermoeglichkeiten/programme/infrastruktur/wgi/geraetegruppenschluessel) into an OWL RDF-based ontology, where each group at each level of the hierarchy (H - Hundertergruppen, Z - Zehnergruppen, E - Einergruppen) is converted into an owl:Class with subclass statements according to the hierarchy. Labels are provided in German (no English translation at time of making).

# Ontology Extension

**Main features**

- 4517 classes in total, no properties  
- 3-tier hierarchy  
  - H (highest level) - 10 Classes  
  - Z (middle level) - 94 Classes  
  - E (lowest level) - 4413 Classes  
- Nested under Instrument class (currently http://purl.obolibrary.org/obo/ERO_0000004)  
- German labels

 - prefix: dfgggs  

[ontology OWL file](ontology/dfgggs_ontology_extension.owl.owl)  
[ontology TTL file](ontology/dfgggs_ontology_extension.ttl)


 
