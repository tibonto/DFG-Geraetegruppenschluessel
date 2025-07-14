# Customizing the Extension using Protégé 

Considering the size and diversity of the DFG GGS, users will likely want to narrow down the size and scope to their specific uses. This is a guide for using Protégé to accomplish this.

**Prerequisites**  

- Protégé installed (https://protegewiki.stanford.edu/wiki/Install_Protege5)  
- This ontology file ([owl](/ontology/dfgggs_ontology_extension.owl) or [ttl](/ontology/dfgggs_ontology_extension.ttl)) to open in Protégé  

**Steps**  

1. Open the ontology file in Protégé  
2. Use the **Entities** tab to browse classes  
3. Export desired classes into a new ontology:  
    - Select **Refractor** from top menu  
    - From the dropdown menu, select **Copy/move/delete axioms...**  
    - Select **Axioms by definition**  
    - Expand class hierarchy and add desired classes to the new ontology. This is done by selecting the class and clicking the [>>] button to add the class into the new list on the right. Multiple classes can be added at once by using shift+click or ctrl+click to select.  
        - **NOTE**: Every class you intend to include in the new ontology must be selected and added. Subclasses will not automatically be imported. Unselected parent classes will only be partially imported (ID only).  
    - When all desired classes are added, click **continue**  
    - Review the axioms (only classes and annotation properties) and click **continue**  
    - Select **Copy axioms** and **continue**  
    - Select **New ontology** and **Finish**  
    - Protégé opens a new window with the new ontology
4. Review and modify new ontology as needed  
    - Delete classes by selecting them and either clicking the **Delete selected classes** icon or **Edit** -> **Delete...**  
    - Reclassify classes by dragging and dropping into the desired parent class
5. Save new ontology file  
    - **File** -> **Save as...** -> select syntax (RDF/XML is good for VIVO import) -> **ok** -> select destination and add file name

**Tips**  

- Quickly expand all classes by selecting **View** from the top menu, then **Expand all** 
- If classes are not rendering properly by rdfs:label (might instead show class ID like "H8000"), check the language setting: go to **View** -> **Custom rendering...**, ensure the **Renderer** tab is selected. Click **Configure...** and check the field next to **Set Language:**. If it's not there, add **de** then click **OK** to save the preferences. The German labels should now render properly.
- **Subclasses are not automatically imported**, and must therefore be selected and added during the import. Multiple classes can be selected at once using shift+click or ctrl+click
- When selecting subclasses (Z or E level) without their parent class, the parent class will be imported with only its ID (ex. H8000). This can be handled later in Protégé by opening the new file and deleting or reclassifying the classes - for example, by dragging and dropping the classes into the desired parent class. 
 