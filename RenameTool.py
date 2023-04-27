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
    cmds.confirmDialog(icn = 'information', message = 'The changes have been made')
    cmds.showWindow()
    
# Define the function that will be called when the user clicks the uppercase button
def rename_uppercase(*args):
    # Get the current selection
    selection = cmds.ls(sl=True)
    if not selection:
        cmds.warning("Please select at least one object to rename.")
        return

    # Renaming
    try:
        for obj in selection:
            cmds.rename(obj, obj.upper())
    except:
        cmds.warning("Could not rename object {0} to {1}.".format(obj, obj.upper()))

# Define the function that will be called when the user clicks the lowercase button
def rename_lowercase(*args):
    # Get the current selection
    selection = cmds.ls(sl=True)
    if not selection:
        cmds.warning("Please select at least one object to rename.")
        return
    
    # Renaming
    try:
        for obj in selection:
            cmds.rename(obj, obj.lower())
    except:
        cmds.warning("Could not rename object {0} to {1}.".format(obj, obj.lower()))
    
# Define the function that will be called when the user clicks the capitalize button
def rename_capitalize(*args):
    # Get the current selection
    selection = cmds.ls(sl=True)
    if not selection:
        cmds.warning("Please select at least one object to rename.")
        return
    
    # Renaming
    try:
        for obj in selection:
            cmds.rename(obj, obj.capitalize())
    except:
        cmds.warning("Could not rename object {0} to {1}.".format(obj, obj.capitalize()))
    
# Create the UI
cmds.window(title="Rename Tool")
cmds.columnLayout(adjustableColumn=True)
cmds.textFieldGrp("prefixField", label="Prefix")
cmds.textFieldGrp("suffixField", label="Suffix")
cmds.textFieldGrp("replaceField", label="Replace")
#cmds.textFieldGrp("replaceWithField", label="Replace With")
cmds.separator(h=4, style='none')  # Empty Space
cmds.rowColumnLayout(nc=3, cw=[(1, 130), (2, 130), (3, 130)], cs=[(1, 0), (2, 5), (3, 5)])
cmds.button(l="U-Case", c=lambda x: rename_uppercase())
cmds.button(l="Capitalize", c=lambda x: rename_capitalize())
cmds.button(l="L-Case", c=lambda x: rename_lowercase())

cmds.separator(h=35, style='none')  # Empty Space
cmds.rowColumnLayout(nc=1, cw=[(1, 130)], cs=[(1,0)])
cmds.button(label="Rename", command=rename_objects)
cmds.showWindow()
