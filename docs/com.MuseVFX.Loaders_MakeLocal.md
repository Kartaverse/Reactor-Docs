# Make Local Button Script
___

## Author
Bryan Ray

## Version
2.5

## Category
Scripts

___

## Description
<p>The "Make Local Button Script" package adds a custom Button Control to your Loader nodes via a Default setting file. You can use the "Make Local" button to copy the media in the Loader into a Comp PathMap managed folder location.</p>
	<p>The script, which will be found in the /Reactor/Deploy/Scripts/Support folder, is easily modified for use in your pipeline. Instructions are in the comments at the beginning of the Loader_MakeLocal.lua file.</p>
	<p>Without customization, the script will copy assets to a sub-folder called 'elements' in the same folder as the .comp file. The composition must be saved before the button will work.</p>
	<p>Because the script is designed to run only from the button, it does not show up in any of the typical script menus within Fusion.</p>
	<p>As a part of the installation process, this Atom will attempt to detect existing Loader default setting files, and if any are found, it will insert the button into those instead of creating a new default. When removed, the button is deleted from all setting files, but any installed Defaults will not be removed, in case you have made additional changes later.

___

## Dependencies

## Deploy

### Common (No Architecture)

> Scripts/Support/Loader_MakeLocal.lua  
> Defaults/Loader_Loader.temp  
