import maya.cmds as cmds

# Define the function that will be called when the user clicks the "Rename" button
def rename_objects(*args):
    prefix = cmds.textFieldGrp("prefixField", q=True, text=True)
    suffix = cmds.textFieldGrp("suffixField", q=True, text=True)
    replace = cmds.textFieldGrp("replaceField", q=True, text=True)
    replace_with = cmds.textFieldGrp("replaceWithField", q=True, text=True)

    selection = cmds.ls(selection=True)

    for obj in selection:
        new_name = obj

        if prefix:
            new_name = prefix + new_name

        if suffix:
            new_name = new_name + suffix

        if replace and replace_with:
            new_name = new_name.replace(replace, replace_with)

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

# Making the UI of the window itself as a class
class RN_Window(object):

	# Constructor
	def __init__(self):

		self.window = 'RN_Window'
		self.title = 'Rename Tool'
		self.size = (400,400)

		# Close old window
		if cmds.window(self.window, exists = True):
			cmds.deleteUI(self.window, window = True)

		# Create new window
		self.window = cmds.window(self.window, title = self.title, widthHeight = self.size)

		# Create the UI
		cmds.columnLayout(adjustableColumn=True)
		cmds.separator(height = 20, width = 100)
		cmds.text('Renaming')
		cmds.separator(height = 20, width = 100)
		cmds.textFieldGrp("prefixField", label="Prefix", columnAlign = [1,'center'])
		cmds.textFieldGrp("suffixField", label="Suffix", columnAlign = [1,'center'])
		cmds.textFieldGrp("replaceField", label="Replace", columnAlign = [1,'center'])
		cmds.textFieldGrp("replaceWithField", label="Replace With", columnAlign = [1,'center'])
		cmds.separator(h=4, style='none')  # Empty Space
		cmds.rowColumnLayout(numberOfColumns = 1, columnWidth = (1,365), cs= [(1,15)])
		cmds.button(label="Rename", command=rename_objects)
		cmds.separator(height = 20, width = 365)
		cmds.rowColumnLayout(numberOfColumns = 3, columnWidth = [(1,115),(2,115),(3,115)], cs=[(1, 0), (2, 10), (3, 10)])
		cmds.button(l="U-Case", c=lambda x: rename_uppercase())
		cmds.button(l="Capitalize", c=lambda x: rename_capitalize())
		cmds.button(l="L-Case", c=lambda x: rename_lowercase())
		cmds.separator(height = 20, width = 365)

		# Display new window
		cmds.showWindow()

myWindow = RN_Window()
