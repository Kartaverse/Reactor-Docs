# Pathmapsky
___

## Category
Scripts/Reactor

## Author
Andrew & Kruno

## Version
1.0

___

## Description
<h1>PathMaps</h1>

<p>Pathmapsky brings a new era of sharable custom PathMap presets to Reactor. It's now easier than ever to quickly backup your custom PathMaps from inside of Resolve Studio's Fusion page, and in Fusion Studio.</p>

<p>Credits: The original Toolbarsky Idea by Kruno, coded by Andrew Hazelden</p>

<h2>Output Locations</h2>

<p>The Pathmapsky "Backup PathMaps" script exports PathMaps to a plain-text JSON format that is stored in the Reactor "PathMaps" folder at:<br>
Reactor:/Deploy/PathMaps/Resolve/<br>
Reactor:/Deploy/PathMaps/Fusion/<br>
</p>

<h2>Extra Details</h2>

<p>The Pathmapsky "Manage PathMaps" script allows you to browse the JSON format PathMaps you have on your system and import them into Fusion. This makes it possible to keep your Resolve Studio's Fusion page and Fusion Studio PathMaps in sync, or to share PathMap JSON files with the rest of your comp team.</p>

<p>The Pathmapsky scripts are accessible in the menu systen under:<br>
<br>
Fusion Studio:<br>
Script &gt; Kruno &gt; Pathmapsky<br>
<br>
Resolve:<br>
Workspace &gt; Script &gt; Kruno &gt; Pathmapsky</p>

<h2>Usage</h2>

<p>1. Start by running the "Backup PathMaps.lua" script in Resolve Studio or Fusion Studio to backup you active toolbar files.</p>

<p>2. Run the "Manage PathMaps.lua" script to view a list of the toolbar JSON files you have on disk.</p>

<p>3. Inside the "Manage PathMaps.lua" script's user interface, select a pathmap item in the list to see its contents in a text preview area. If you wish to load the selected toolbar into the active Resolve/Fusion system, press the "Import PathMap" button.</p>

<p>Note: The &#91;x&#93; Show New or Changed PathMap checkbox at the top of the window filters the tree view contents so you only see the PathMap do not exist in your copy of Fusion.</p>

<p>Note: If you wish, you can manually back up your "Fusion.prefs" file before you use the Pathmapsky script. The PathMap entries are located in the Lua table structure at the hierarchy of "Global.Paths.Map"</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.Kruno.Pathmapsky.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.Kruno.Pathmapsky)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Pathmapsky/Docs/Kruno/Pathmapsky.html?ref_type=heads">Docs/Kruno/Pathmapsky.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Pathmapsky/PathMaps/Fusion/Fonts_PathMap.json?ref_type=heads">PathMaps/Fusion/Fonts_PathMap.json</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Pathmapsky/Scripts/Comp/Kruno/Pathmapsky/Backup PathMaps.lua?ref_type=heads">Scripts/Comp/Kruno/Pathmapsky/Backup PathMaps.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Pathmapsky/Scripts/Comp/Kruno/Pathmapsky/Manage PathMaps.lua?ref_type=heads">Scripts/Comp/Kruno/Pathmapsky/Manage PathMaps.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.Kruno.Pathmapsky/Scripts/Comp/Kruno/Pathmapsky/Open PathMaps Folder.lua?ref_type=heads">Scripts/Comp/Kruno/Pathmapsky/Open PathMaps Folder.lua</a></li>
</ul>
