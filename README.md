# PowerSave
A powerful saving tool.

## Installation
Go to Blender preferences, Add-ons, then click `Install...` and choose the zip file.  
Set your `Base Folder` in the PowerSave preferences. Your powersaved blends go there.  

## Usage
After installation you have a new icon in the 3D view top bar.  
It is red, when your file is unsaved, and turns green, when your file is saved.  
Gray means saved, but with unsaved changes. There are color options in the preferences.  
Clicking the icon opens the PowerSave panel.  

The `PowerSave` button will save your file using the project name given in the text field,  
or a timestamp (configurable in the preferences), and saves it to your `Base Folder`.  
If you use `PowerSave` with a previously saved file, it will use its location.  
If the file already exists, clicking `PowerSave` will do an incremental save, which adds a number at the end of the file name.  
You can use slash to create a directory within your `Base Folder` or current directory.  
The arrow icons open the previous/next iteration of your project.  

The `Autosave Interval` is how many minutes to wait between autosaves.  
It autosaves to the `Autosave Folder` you set in the PowerSave preferences.  
Both absolute and relative paths are supported, and it can save over the current file.  
If you open a file and there is a newer autosave available, you will be prompted to open it.  
If you click OK on that prompt, it will open the autosave and save it as an increment of your original file.  

## Links
- [PowerSave on GitHub](https://github.com/bonjorno7/PowerSave)
- [PowerSave on Gumroad](https://bonjorno7.gumroad.com/l/powersave)
- [PowerSave on BlenderMarket](https://blendermarket.com/products/powersave)
