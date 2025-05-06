# Pipe EXR Management
___

## Category
Tools/Flow

## Author
Dominik Bargiel

## Version
1.3

___

## Description
<h1>Pipe – EXR Manager for Fusion</h1>

<p>Pipe is a toolset designed to improve Fusion’s handling of multi-pass EXRs, making compositing more efficient and organized. It automates EXR versioning, simplifies Loader management, and provides a more flexible way to work with render passes.</p>

<a href="https://youtu.be/DwK4zphqj2o">Watch the Pipe EXR Manager tutorial on YouTube</a>

<h2>Key Features:</h2>
<ul>
<li><strong>EXR Pass Management</strong> – Access all EXR passes from any Pipe node, reducing node clutter.</li>
<li><strong>Auto-Updates for New Passes</strong> – Automatically adds new passes when an EXR is updated.</li>
<li><strong>Path Handling & Organization</strong> – Easily update and structure paths for all loaders at once.</li>
<li><strong>Batch Version Control</strong> – Swap versions across multiple Loaders with ease.</li>
<li><strong>Cryptomatte Support</strong> – Use multi-part EXRs for Cryptomattes.</li>
<li><strong>Root Folder Handling</strong> – Links passes in separate folders (e.g., /specular, /refraction).</li>
<li><strong>Centralized UI</strong> – Manage everything in one place.</li>
</ul>

<h2>How to Use:</h2>
<ol>
<li><strong>Create a Pipe Group:</strong> Select the Loader or Loaders you want to group and run the <strong>PipeCreate.lua</strong> script with <strong>CTRL+ALT+P</strong>. You can set your desired group name and root path.</li>
<li><strong>Unpack EXR to separate Loaders</strong> Open Pipe Manager on the Pipe node and click "Update All". It will work like hosSplitExrUltra</li>
<li><strong>Connect the Pipe Node:</strong> Copy the created Pipe node. It holds data for all tools in the Pipe Group, giving you access to all passes from grouped EXRs for a cleaner workflow.</li>
<li><strong>Manage Groups via Pipe Manager:</strong> Open the Pipe Manager from the Fuse UI and easily swap versions (e.g., <strong>V001</strong>) or paths for the entire group.</li>
<li><strong>Use PipeCryptomatte:</strong> For multipart Cryptomattes, connect to any Pipe node in a group and click "Initialize".</li>
</ol>

___

## Donation
The author of the atom has suggested a donation of "1".  
You can donate using the URL: <a href="paypal.me/dominikbargiel">paypal.me/dominikbargiel</a>

## Download

Download a zipped atom package for offline installation:
> [com.DominikBargiel.Pipe_EXR_Management.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.DominikBargiel.Pipe_EXR_Management)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Config/Pipe/Pipe_shortcuts.fu?ref_type=heads">Config/Pipe/Pipe_shortcuts.fu</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Config/Pipe/Pipe_tile_and_color.fu?ref_type=heads">Config/Pipe/Pipe_tile_and_color.fu</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Config/Pipe/Pipecryptomatte_shortcuts.fu?ref_type=heads">Config/Pipe/Pipecryptomatte_shortcuts.fu</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Fuses/Flow/Pipe.fuse?ref_type=heads">Fuses/Flow/Pipe.fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Fuses/Matte/PipeCryptomatte.fuse?ref_type=heads">Fuses/Matte/PipeCryptomatte.fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Modules/Lua/Pipe/ErrorHandler.lua?ref_type=heads">Modules/Lua/Pipe/ErrorHandler.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Modules/Lua/Pipe/GroupValidation.lua?ref_type=heads">Modules/Lua/Pipe/GroupValidation.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Modules/Lua/Pipe/PathUtils.lua?ref_type=heads">Modules/Lua/Pipe/PathUtils.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Modules/Lua/Pipe/PipeCryptomatte_utilities.lua?ref_type=heads">Modules/Lua/Pipe/PipeCryptomatte_utilities.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Modules/Lua/Pipe/Pipetest_cryptomatte_utilities.lua?ref_type=heads">Modules/Lua/Pipe/Pipetest_cryptomatte_utilities.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Scripts/Utility/Pipe/PipeCopy.lua?ref_type=heads">Scripts/Utility/Pipe/PipeCopy.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Scripts/Utility/Pipe/PipeCreate.lua?ref_type=heads">Scripts/Utility/Pipe/PipeCreate.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Scripts/Utility/Pipe/PipeManager.lua?ref_type=heads">Scripts/Utility/Pipe/PipeManager.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Pipe_EXR_Management/Scripts/Utility/Pipe/PipePaste.lua?ref_type=heads">Scripts/Utility/Pipe/PipePaste.lua</a></li>
</ul>
