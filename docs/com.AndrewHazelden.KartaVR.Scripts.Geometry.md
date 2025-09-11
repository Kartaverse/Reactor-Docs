# KartaVR Scripts | Geometry
___

## Category
Kartaverse/KartaVR/Scripts

## Author
Andrew Hazelden

## Version
5.85

___

## Description
<p>The KartaVR Geometry scripts allow you to pass your media to 3rd party 3D tools like <a href="http://www.cloudcompare.org">CloudCompare</a>, <a href="https://github.com/wjakob/instant-meshes">Instant Meshes</a>, and <a href="http://www.meshlab.net/">MeshLab</a>. These scripts are accesed using the "Script &gt; KartaVR &gt; Geometry &gt; " menu in Fusion.</p>

<p>The "Send Geometry to Lightwave Modeler.lua" script takes your FBXMesh3D and AlembicMesh3D node content and opens it up in Lightwave for editing. This speeds up the process of doing a quick .OBJ model edit such as UV layout change.</p>

<p>The "Send Geometry to usdview" script takes AlembicMesh3D nodes that are selected in the Nodes view and sends the .abc models to usdview. The usdview program needs to be installed on the system and listed in the $PATH environment variable. usdview is primarily used to examine PIXAR OpenUSD (USDC/USDA) format scene graphs but it can also work with Alembic models too.</p>

<p>The "Reload Alembic Scene", "Reload FBX Scene", and "Reload PSD Layers" scripts work on macOS systems and allows you to use <a href="https://www.keyboardmaestro.com/main/">Keyboard Maestro</a> and the "KartaVR Macros.kmmacros" file to instantly re-import scenes into Fusion v9.</p>

<p>The "Export Point Cloud" script has been moved to a new KartaVR "Virtual Productions" atom package.</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.KartaVR.Scripts.Geometry.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Scripts/Comp/KartaVR/Geometry/Send Geometry to CloudCompare Viewer.lua?ref_type=heads">Scripts/Comp/KartaVR/Geometry/Send Geometry to CloudCompare Viewer.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Scripts/Comp/KartaVR/Geometry/Send Geometry to CloudCompare.lua?ref_type=heads">Scripts/Comp/KartaVR/Geometry/Send Geometry to CloudCompare.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Scripts/Comp/KartaVR/Geometry/Send Geometry to Instant Meshes.lua?ref_type=heads">Scripts/Comp/KartaVR/Geometry/Send Geometry to Instant Meshes.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Scripts/Comp/KartaVR/Geometry/Send Geometry to Lightwave Modeler.lua?ref_type=heads">Scripts/Comp/KartaVR/Geometry/Send Geometry to Lightwave Modeler.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Scripts/Comp/KartaVR/Geometry/Send Geometry to MeshLab.lua?ref_type=heads">Scripts/Comp/KartaVR/Geometry/Send Geometry to MeshLab.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Scripts/Comp/KartaVR/Geometry/Send Geometry to usdview.lua?ref_type=heads">Scripts/Comp/KartaVR/Geometry/Send Geometry to usdview.lua</a></li>
</ul>

### Linux

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Linux/Scripts/Comp/KartaVR/Geometry/Send Geometry to AC3D.lua?ref_type=heads">Scripts/Comp/KartaVR/Geometry/Send Geometry to AC3D.lua</a></li>

### macOS

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Mac/Bin/KartaVR/bonus/Keyboard Maestro Macros/KartaVR Macros.kmmacros?ref_type=heads">Bin/KartaVR/bonus/Keyboard Maestro Macros/KartaVR Macros.kmmacros</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Mac/Scripts/Comp/KartaVR/Geometry/Reload Alembic Scene.lua?ref_type=heads">Scripts/Comp/KartaVR/Geometry/Reload Alembic Scene.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Mac/Scripts/Comp/KartaVR/Geometry/Reload FBX Scene.lua?ref_type=heads">Scripts/Comp/KartaVR/Geometry/Reload FBX Scene.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Mac/Scripts/Comp/KartaVR/Geometry/Reload PSD Layers.lua?ref_type=heads">Scripts/Comp/KartaVR/Geometry/Reload PSD Layers.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Mac/Scripts/Comp/KartaVR/Geometry/Send Geometry to AC3D.lua?ref_type=heads">Scripts/Comp/KartaVR/Geometry/Send Geometry to AC3D.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Mac/Scripts/kartavr.scriptlib?ref_type=heads">Scripts/kartavr.scriptlib</a></li>

### Windows

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.Geometry/Windows/Scripts/Comp/KartaVR/Geometry/Send Geometry to AC3D.lua?ref_type=heads">Scripts/Comp/KartaVR/Geometry/Send Geometry to AC3D.lua</a></li>
