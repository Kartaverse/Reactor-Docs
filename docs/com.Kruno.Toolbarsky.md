# Toolbarsky
___

## Category
Scripts/Reactor

## Author
Andrew & Kruno

## Version
1.0

___

## Description
<h1>Toolbarsky</h1>

<p>Toolbarsky brings a new era of sharable custom toolbars to Reactor. It's now easier than ever to quickly backup your custom Toolbars from inside of Resolve Studio's Fusion page, and in Fusion Studio.</p>

<p>Credits: Idea by Kruno, coded by Andrew Hazelden</p>

<h2>Output Locations</h2>

<p>The Toolbarsky "Backup Toolbars" script exports toolbars to a plain-text JSON format that is stored in the Reactor "Toolbars" folder at:<br>
Reactor:/Deploy/Toolbars/Resolve/<br>
Reactor:/Deploy/Toolbars/Fusion/<br>
</p>

<h2>Extra Details</h2>

<p>The Toolbarsky "Manage Toolbars" script allows you to browse the JSON format toolbars you have on your system and import them into Fusion. This makes it possible to keep your Resolve Studio's Fusion page and Fusion Studio toolbars in sync, or to share toolbar JSON files with the rest of your comp team.</p>

<p>The Toolbarsky scripts are accessible in the menu systen under:<br>
<br>
Fusion Studio:<br>
Script &gt; Kruno &gt; Toolbarsky<br>
<br>
Resolve:<br>
Workspace &gt; Script &gt; Kruno &gt; Toolbarsky</p>

<h2>Usage</h2>

<p>1. Start by running the "Backup Toolbars.lua" script in Resolve Studio or Fusion Studio to backup you active toolbar files.</p>

<p>2. Run the "Manage Toolbars.lua" script to view a list of the toolbar JSON files you have on disk.</p>

<p>3. Inside the "Manage Toolbars.lua" script's user interface, select a toolbar item in the list to see its contents in a text preview area. If you wish to load the selected toolbar into the active Resolve/Fusion system, press the "Import Toolbar" button.</p>

<p>Note: If you wish, you can manually back up your "Fusion.prefs" file before you use the Toolbarsky script. The Toolbar entries are located in the Lua table structure at the hierarchy of "Global.ActionStrip.Toolbars"</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.Kruno.Toolbarsky.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.Kruno.Toolbarsky)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Toolbarsky/Docs/Kruno/Toolbarsky.html?ref_type=heads">Docs/Kruno/Toolbarsky.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Toolbarsky/Scripts/Comp/Kruno/Toolbarsky/Backup Toolbars.lua?ref_type=heads">Scripts/Comp/Kruno/Toolbarsky/Backup Toolbars.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Toolbarsky/Scripts/Comp/Kruno/Toolbarsky/Manage Toolbars.lua?ref_type=heads">Scripts/Comp/Kruno/Toolbarsky/Manage Toolbars.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Toolbarsky/Scripts/Comp/Kruno/Toolbarsky/Open Toolbars Folder.lua?ref_type=heads">Scripts/Comp/Kruno/Toolbarsky/Open Toolbars Folder.lua</a></li>
</ul>
