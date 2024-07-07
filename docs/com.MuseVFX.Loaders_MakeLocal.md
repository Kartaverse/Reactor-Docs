# Make Local Button Script
___

## Category
Scripts

## Author
Bryan Ray

## Version
2.5

___

## Description
<p>The "Make Local Button Script" package adds a custom Button Control to your Loader nodes via a Default setting file. You can use the "Make Local" button to copy the media in the Loader into a Comp PathMap managed folder location.</p>
	<p>The script, which will be found in the /Reactor/Deploy/Scripts/Support folder, is easily modified for use in your pipeline. Instructions are in the comments at the beginning of the Loader_MakeLocal.lua file.</p>
	<p>Without customization, the script will copy assets to a sub-folder called 'elements' in the same folder as the .comp file. The composition must be saved before the button will work.</p>
	<p>Because the script is designed to run only from the button, it does not show up in any of the typical script menus within Fusion.</p>
	<p>As a part of the installation process, this Atom will attempt to detect existing Loader default setting files, and if any are found, it will insert the button into those instead of creating a new default. When removed, the button is deleted from all setting files, but any installed Defaults will not be removed, in case you have made additional changes later.

___

## Donation
The author of the atom has suggested a donation of "$2 USD".  
You can donate using the URL: <a href="paypal.me/BryanRayVFX">paypal.me/BryanRayVFX</a>
## Download

Download a zipped atom package for offline installation:
> [com.MuseVFX.Loaders_MakeLocal.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.MuseVFX.Loaders_MakeLocal)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.MuseVFX.Loaders_MakeLocal/Scripts/Support/Loader_MakeLocal.lua?ref_type=heads">Scripts/Support/Loader_MakeLocal.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.MuseVFX.Loaders_MakeLocal/Defaults/Loader_Loader.temp?ref_type=heads">Defaults/Loader_Loader.temp</a></li>
</ul>
