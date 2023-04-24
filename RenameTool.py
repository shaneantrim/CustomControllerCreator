import maya.cmds as cmds

# Define the function that will be called when the user clicks the "Rename" button
def rename_objects(*args):
    # Get the current selection
    selection = cmds.ls(selection=True)
    if not selection:
        cmds.warning("Please select at least one object to rename.")
        return
    
    # Get the user's input from the UI
    prefix = cmds.textFieldGrp("prefixField", query=True, text=True)
    suffix = cmds.textFieldGrp("suffixField", query=True, text=True)
    replace = cmds.textFieldGrp("replaceField", query=True, text=True)
    #replace_with = cmds.textFieldGrp("replaceWithField", query=True, text=True)
    
    # Loop through each selected object and rename it
    for obj in selection:
        # Generate the new name based on the user's input
        new_name = obj
        if prefix:
            new_name = prefix + '_' + new_name
        if suffix:
            new_name = new_name + '_' + suffix
        if replace:
            new_name = new_name.replace(obj,replace)
        
        # Rename the object
        try:
            cmds.rename(obj, new_name)
        except:
            cmds.warning("Could not rename object {0} to {1}.".format(obj, new_name))
       
    # Confirm message
    cmds.confirmDialog(icn = 'information', message = 'Done!')
    cmds.showWindow()

# Create the UI
cmds.window(title="Rename Tool")
cmds.columnLayout(adjustableColumn=True)
cmds.textFieldGrp("prefixField", label="Prefix")
cmds.textFieldGrp("suffixField", label="Suffix")
cmds.textFieldGrp("replaceField", label="Replace")
#cmds.textFieldGrp("replaceWithField", label="Replace With")
cmds.button(label="Rename", command=rename_objects)
cmds.showWindow()
