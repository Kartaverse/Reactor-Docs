# Variablesky
___

## Category
Scripts/Reactor

## Author
Andrew & Kruno

## Version
1.0

___

## Description
<h1>Variablesky</h1>

<p>Variablesky brings a new era of sharable custom Variable Map presets to Reactor. It's now easier than ever to quickly backup your custom Variable Maps from inside of Resolve Studio's Fusion page, and in Fusion Studio.</p>

<p>Credits: The original Toolbarsky Idea by Kruno, coded by Andrew Hazelden</p>

<h2>Output Locations</h2>

<p>The Variablesky "Backup VariableMaps" script exports Variable Maps to a plain-text JSON format that is stored in the Reactor "VariableMaps" folder at:<br>
Reactor:/Deploy/VariableMaps/Resolve/<br>
Reactor:/Deploy/VariableMaps/Fusion/<br>
</p>

<h2>Extra Details</h2>

<p>The Variablesky "Manage VariableMaps" script allows you to browse the JSON format VariableMaps you have on your system and import them into Fusion. This makes it possible to keep your Resolve Studio's Fusion page and Fusion Studio PathMaps in sync, or to share VariableMap JSON files with the rest of your comp team.</p>

<p>The Variablesky scripts are accessible in the menu systen under:<br>
<br>
Fusion Studio:<br>
Script &gt; Kruno &gt; Variablesky<br>
<br>
Resolve:<br>
Workspace &gt; Script &gt; Kruno &gt; Variablesky</p>

<h2>Usage</h2>

<p>1. Start by running the "Backup VariableMaps.lua" script in Resolve Studio or Fusion Studio to backup you active variable map files.</p>

<p>2. Run the "Manage VariableMaps.lua" script to view a list of the variable map JSON files you have on disk.</p>

<p>3. Inside the "Manage VariableMaps.lua" script's user interface, select an item in the list to see its contents in a text preview area. If you wish to load the selected variable map into the active Resolve/Fusion system, press the "Import VariableMap" button.</p>

<p>Note: The &#91;x&#93; Show New or Changed VariableMap checkbox at the top of the window filters the tree view contents so you only see the VariableMaps that do not exist in your copy of Fusion.</p>

<p>Note: If you wish, you can manually back up your "Fusion.prefs" file before you use the Variablesky script. The VariableMap entries are located in the Lua table structure at the hierarchy of "Global.Variables.Map"</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.Kruno.Variablesky.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.Kruno.Variablesky)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Variablesky/Docs/Kruno/Variablesky.html?ref_type=heads">Docs/Kruno/Variablesky.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Variablesky/Scripts/Comp/Kruno/Variablesky/Backup VariableMaps.lua?ref_type=heads">Scripts/Comp/Kruno/Variablesky/Backup VariableMaps.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Variablesky/Scripts/Comp/Kruno/Variablesky/Manage VariableMaps.lua?ref_type=heads">Scripts/Comp/Kruno/Variablesky/Manage VariableMaps.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Variablesky/Scripts/Comp/Kruno/Variablesky/Open VariableMaps Folder.lua?ref_type=heads">Scripts/Comp/Kruno/Variablesky/Open VariableMaps Folder.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Variablesky/VariableMaps/Fusion/metadata_VariableMap.json?ref_type=heads">VariableMaps/Fusion/metadata_VariableMap.json</a></li>
</ul>
