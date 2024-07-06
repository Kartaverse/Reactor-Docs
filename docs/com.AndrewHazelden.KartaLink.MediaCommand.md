# KartaLink | Media Command
___

## Author
 : Andrew Hazelden

## Version
 : v5.73

## Category
 : Kartaverse/KartaLink/Scripts
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

## Dependencies


___

## Deploy

### Common (No Architecture)

> Comps/Kartaverse/KartaLink/Media Command/Clip Lua Table to ScriptVal.comp  
> Docs/Kartaverse/KartaLink/Media Command/Images/command_script.png  
> Docs/Kartaverse/KartaLink/Media Command/Images/edit_go_buttons.png  
> Docs/Kartaverse/KartaLink/Media Command/Images/example_clip_lua_table_to_scriptval.png  
> Docs/Kartaverse/KartaLink/Media Command/Images/fusion_settings_script.png  
> Docs/Kartaverse/KartaLink/Media Command/Images/media_command.png  
> Docs/Kartaverse/KartaLink/Media Command/Images/script_send_to_ptgui.png  
> Docs/Kartaverse/KartaLink/Media Command/Images/search_field.png  
> Docs/Kartaverse/KartaLink/Media Command/Images/select_buttons.png  
> Docs/Kartaverse/KartaLink/Media Command/Images/type_combomenu.png  
> Docs/Kartaverse/KartaLink/Media Command/Images/view_buttons.png  
> Docs/Kartaverse/KartaLink/Media Command/Media Command.md  
> Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Audio.png  
> Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Bin.png  
> Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Compound.png  
> Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Fusion.png  
> Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Generator.png  
> Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Geometry.png  
> Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Stereo.png  
> Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Still.png  
> Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Subtitle.png  
> Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Timeline.png  
> Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Video + Audio.png  
> Scripts/Edit/Kartaverse/KartaLink/Icons/Type/Video.png  
> Scripts/Edit/Kartaverse/KartaLink/Media Command.lua  
> Scripts/MediaCommand/Examples/Lua/Copy File Name.lua  
> Scripts/MediaCommand/Examples/Lua/Copy File Path.lua  
> Scripts/MediaCommand/Examples/Lua/Copy JSON.lua  
> Scripts/MediaCommand/Examples/Lua/Copy Lua Table.lua  
> Scripts/MediaCommand/Examples/Lua/List Args.lua  
> Scripts/MediaCommand/Examples/Lua/List Clips.lua  
> Scripts/MediaCommand/Examples/Python/List Args.py  
> Scripts/MediaCommand/Examples/Python/List Clips.py  
> Scripts/MediaCommand/XR/Add MediaIn to Comp.lua  
> Scripts/MediaCommand/XR/Send to DeoVR.lua  
> Scripts/MediaCommand/XR/Send to PTGui.lua  
