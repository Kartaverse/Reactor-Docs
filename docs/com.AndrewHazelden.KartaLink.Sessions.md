# KartaLink | Comp Sessions
___

## Category
Kartaverse/KartaLink/Scripts

## Author
Andrew Hazelden

## Version
5.75

___

## Description
<h2>Comp Session</h2>

<p>The "File &gt; Sessions &gt;" menu allows you to quickly load and save a snapshot of the open .comp tabs that are active in Fusion Studio Standalone. The node selection state is restored for each of the comps as well. This makes it easy to return to an earlier work session.</p>

<p>This approach lets you hop back into a multi-document compositing session and have all your comp work loaded up, just like it was when you saved the previous session.</p>

<h2>Menu Entries</h2>

<p>The "Config:/Menus/Kartaverse Sessions.fu" file adds the following menu entries to Fusion Studio Standalone:</p>

<pre>File > Sessions:
- Restore Session
- Load Session...
- --------------------
- Save Session
- Save Session As...
- --------------------
- Close Session
</pre>

<h2>Usage</h2>

<p>The "Restore Session" menu loads the most recently used session file. Existing comp tabs will be saved and closed first.</p>
<p>The "Load Session..." menu item lets you open up pre-existing .json based session files. Existing comp tabs will be saved and closed first.</p>
<p>The "Save Session" menu item lets you re-save the active .json based session files to disk. This will refresh the active comp tabs and node selection values.</p>
<p>The "Save Sessions As..." menu item lets you save your session to a different .json based session filename on disk.</p>
<p>The "Close Sessions" menu item closes all of the open comp tabs. You are asked to save each .comp file if there are any changes.</p>

<h2>Session Files</h2>

<p>Comp session files are saved in a .json file format. The default comp session document storage path is:<br>
<a href="file://Reactor:/Deploy/Scripts/Support/Kartaverse/Sessions/">Reactor://Deploy/Scripts/Support/Kartaverse/Sessions/</a></p>


___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.KartaLink.Sessions.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.KartaLink.Sessions)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.Sessions/Config/Menus/Kartaverse Sessions.fu?ref_type=heads">Config/Menus/Kartaverse Sessions.fu</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.Sessions/Docs/Kartaverse/KartaLink/Sessions/Images/file_menu.png?ref_type=heads">Docs/Kartaverse/KartaLink/Sessions/Images/file_menu.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.Sessions/Docs/Kartaverse/KartaLink/Sessions/Sessions.html?ref_type=heads">Docs/Kartaverse/KartaLink/Sessions/Sessions.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.Sessions/Docs/Kartaverse/KartaLink/Sessions/Sessions.md?ref_type=heads">Docs/Kartaverse/KartaLink/Sessions/Sessions.md</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.Sessions/Scripts/Comp/KartaLink/Sessions/Open Sessions Docs Folder.lua?ref_type=heads">Scripts/Comp/KartaLink/Sessions/Open Sessions Docs Folder.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.Sessions/Scripts/Comp/KartaLink/Sessions/Open Sessions Folder.lua?ref_type=heads">Scripts/Comp/KartaLink/Sessions/Open Sessions Folder.lua</a></li>
</ul>
