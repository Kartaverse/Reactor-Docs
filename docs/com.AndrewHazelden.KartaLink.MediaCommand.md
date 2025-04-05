# KartaLink | Media Command
___

## Category
Kartaverse/KartaLink/Scripts

## Author
Andrew Hazelden

## Version
5.76

___

## Description
<p>Kartaverse "Media Command" is a scriptable interface for batch processing content that resides in your Resolve Media Pool. This streamlines the process of selecting footage, and running automation scripts on those specific items.</p>

<p>When Media Command is launched it automatically scans for Lua and Python scripts that are located on your hard disk inside the "Reactor:/Deploy/Scripts/MediaCommand/" folder. These items are added to the "Command Script" ComboMenu in the interface.</p>

<p>If you are a long time Fusion user, you will find the Media Command script was designed to give your Media page content management operations the same power and flexibility as you have with a Fusion page "tool" script in the Fusion nodes view context.</p>

<p><h2>Script Usage:</h2></p>

<p>Step 1. Place your custom .lua or .py scripts into the "Reactor:/Deploy/Scripts/MediaCommand/" folder.</p>

<p>Step 2. Launch the Media Command script from the Resolve "Workspaces > Scripts > Edit > Kartaverse > KartaLink > Media Command" menu entry.</p>

<p>Step 3. Select the footage you would like to batch process by clicking on the tree view row entries in the Media Command window. At the moment you need to click on the actual "text" words on the row to toggle the "selected" checkbox state.</p>

<p>Step 4. Choose a script you would like to run on the selected media using the "Command Script" ComboMenu, then press the "Go" button.</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.KartaLink.MediaCommand.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.KartaLink.MediaCommand)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Comps/Kartaverse/KartaLink/Media Command/Clip Lua Table to ScriptVal.comp?ref_type=heads">Comps/Kartaverse/KartaLink/Media Command/Clip Lua Table to ScriptVal.comp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Docs/Kartaverse/KartaLink/Media Command/Images/command_script.png?ref_type=heads">Docs/Kartaverse/KartaLink/Media Command/Images/command_script.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Docs/Kartaverse/KartaLink/Media Command/Images/edit_go_buttons.png?ref_type=heads">Docs/Kartaverse/KartaLink/Media Command/Images/edit_go_buttons.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Docs/Kartaverse/KartaLink/Media Command/Images/example_clip_lua_table_to_scriptval.png?ref_type=heads">Docs/Kartaverse/KartaLink/Media Command/Images/example_clip_lua_table_to_scriptval.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Docs/Kartaverse/KartaLink/Media Command/Images/fusion_settings_script.png?ref_type=heads">Docs/Kartaverse/KartaLink/Media Command/Images/fusion_settings_script.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Docs/Kartaverse/KartaLink/Media Command/Images/media_command.png?ref_type=heads">Docs/Kartaverse/KartaLink/Media Command/Images/media_command.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Docs/Kartaverse/KartaLink/Media Command/Images/script_send_to_ptgui.png?ref_type=heads">Docs/Kartaverse/KartaLink/Media Command/Images/script_send_to_ptgui.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Docs/Kartaverse/KartaLink/Media Command/Images/search_field.png?ref_type=heads">Docs/Kartaverse/KartaLink/Media Command/Images/search_field.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Docs/Kartaverse/KartaLink/Media Command/Images/select_buttons.png?ref_type=heads">Docs/Kartaverse/KartaLink/Media Command/Images/select_buttons.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Docs/Kartaverse/KartaLink/Media Command/Images/type_combomenu.png?ref_type=heads">Docs/Kartaverse/KartaLink/Media Command/Images/type_combomenu.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Docs/Kartaverse/KartaLink/Media Command/Images/view_buttons.png?ref_type=heads">Docs/Kartaverse/KartaLink/Media Command/Images/view_buttons.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Docs/Kartaverse/KartaLink/Media Command/Media Command.md?ref_type=heads">Docs/Kartaverse/KartaLink/Media Command/Media Command.md</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Audio.png?ref_type=heads">Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Audio.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Bin.png?ref_type=heads">Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Bin.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Compound.png?ref_type=heads">Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Compound.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Fusion.png?ref_type=heads">Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Fusion.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Generator.png?ref_type=heads">Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Generator.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Geometry.png?ref_type=heads">Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Geometry.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Stereo.png?ref_type=heads">Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Stereo.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Still.png?ref_type=heads">Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Still.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Subtitle.png?ref_type=heads">Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Subtitle.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Timeline.png?ref_type=heads">Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Timeline.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Video + Audio.png?ref_type=heads">Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Video + Audio.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Video.png?ref_type=heads">Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Video.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/Edit/Kartaverse/KartaLink/Media Command.lua?ref_type=heads">Scripts/Edit/Kartaverse/KartaLink/Media Command.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/MediaCommand/Examples/Lua/Copy File Name.lua?ref_type=heads">Scripts/MediaCommand/Examples/Lua/Copy File Name.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/MediaCommand/Examples/Lua/Copy File Path.lua?ref_type=heads">Scripts/MediaCommand/Examples/Lua/Copy File Path.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/MediaCommand/Examples/Lua/Copy JSON.lua?ref_type=heads">Scripts/MediaCommand/Examples/Lua/Copy JSON.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/MediaCommand/Examples/Lua/Copy Lua Table.lua?ref_type=heads">Scripts/MediaCommand/Examples/Lua/Copy Lua Table.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/MediaCommand/Examples/Lua/List Args.lua?ref_type=heads">Scripts/MediaCommand/Examples/Lua/List Args.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/MediaCommand/Examples/Lua/List Clips.lua?ref_type=heads">Scripts/MediaCommand/Examples/Lua/List Clips.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/MediaCommand/Examples/Python/List Args.py?ref_type=heads">Scripts/MediaCommand/Examples/Python/List Args.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/MediaCommand/Examples/Python/List Clips.py?ref_type=heads">Scripts/MediaCommand/Examples/Python/List Clips.py</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/MediaCommand/XR/Add MediaIn to Comp.lua?ref_type=heads">Scripts/MediaCommand/XR/Add MediaIn to Comp.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/MediaCommand/XR/Send to DeoVR.lua?ref_type=heads">Scripts/MediaCommand/XR/Send to DeoVR.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaLink.MediaCommand/Scripts/MediaCommand/XR/Send to PTGui.lua?ref_type=heads">Scripts/MediaCommand/XR/Send to PTGui.lua</a></li>
</ul>
