# KartaVR DragDrop
___

## Category
Kartaverse/KartaVR/DragDrop

## Author
Andrew Hazelden

## Version
5.85

___

## Description
<p>The &quot;KartaVR DragDrop&quot; atom package adds support for new "Drag and Drop" file type handlers to Fusion/Resolve v16-19+.</p>

<p>The &quot;KartaVR Comp DragDrop.fu&quot; file allows you to import a Fusion .comp file by dragging it into the Nodes view from a desktop Explorer/Finder/Nautilus folder browsing window. This is a quick way to merge in external Fusion .comp documents into an existing open foreground composite and is very handy for Resolve users who work with Media Pool based Fusion comps, or Timeline based Fusion comps.</p>

<p>The &quot;KartaVR PTGui DragDrop.fu&quot; file allows the Kartaverse "PT" Panotools data nodes to easily access PTGui Pro v11-12+ .pts documents that are dragged into the Nodes view from a desktop Explorer/Finder/Nautilus folder browsing window.</p>

<p>The &quot;KartaVR PointCloud DragDrop.fu&quot; file allows .xyz point cloud documents to be imported as PointCloud3D nodes when the .xyz files are dragged into the Nodes view from a desktop Explorer/Finder/Nautilus folder browsing window.</p>

<p>Note: After you install the &quot;KartaVR DragDrop&quot; package in Reactor, you will need to restart the Fusion/Resolve program once so the new .fu files are loaded during Fusion's startup phase.</p>

<h2>Where do I find the "KartaVR DragDrop" file in on disk?</h2>

<p>The "KartaVR DragDrop" files are installed by Reactor to the local folder of:<br>
<a href="file://Reactor:/Deploy/Config/DragDrop/">Reactor:/Deploy/Config/DragDrop/</a></p>


___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.KartaVR.DragDrop.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.KartaVR.DragDrop)  

## Dependencies

> [com.AndrewHazelden.KartaVR.Scripts.Stitching](com.AndrewHazelden.KartaVR.Scripts.Stitching.md)  
## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.DragDrop/Config/DragDrop/KartaVR Comp DragDrop.fu?ref_type=heads">Config/DragDrop/KartaVR Comp DragDrop.fu</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.DragDrop/Config/DragDrop/KartaVR PTGui DragDrop.fu?ref_type=heads">Config/DragDrop/KartaVR PTGui DragDrop.fu</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.DragDrop/Config/DragDrop/KartaVR PointCloud DragDrop.fu?ref_type=heads">Config/DragDrop/KartaVR PointCloud DragDrop.fu</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.DragDrop/Scripts/Comp/KartaVR/DragDrop/Comp Import.lua?ref_type=heads">Scripts/Comp/KartaVR/DragDrop/Comp Import.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.DragDrop/Scripts/Comp/KartaVR/DragDrop/PointCloud Import.lua?ref_type=heads">Scripts/Comp/KartaVR/DragDrop/PointCloud Import.lua</a></li>
</ul>
