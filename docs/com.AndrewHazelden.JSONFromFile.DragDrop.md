# Vonk DragDrop | vJSONFromFile
___

## Category
Kartaverse/Vonk Ultra/DragDrop

## Author
AndrewHazelden

## Version
5.85

___

## Description
<p>The "Vonk vJSONFromFile DragDrop.fu" file allows you to import a .json file by dragging it into the Nodes view from a desktop Explorer/Finder/Linux folder browsing window. This is a quick way to bring external data records into your Resolve/Fusion composite. The DragDrop file supports dragging in multiple JSON elements at the same time, and each item will be imported into a separate vJSONFromFile node.</p>

<p>If the JSON file is a Kartaverse Lens Profile .json then a kvrFisheyeStereo node is added automatically.</p>

<p>If the JSON file is a Kartaverse Comp Session .json then a pre-existing MDI (multi-document interface) compositing workspace session is restored where the .comp files are loaded automatically and the active node based selection is restored.</p>

<p>This DragDrop file has a dependency on the Vonk FusionJSON atom package.</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.JSONFromFile.DragDrop.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.JSONFromFile.DragDrop)  

## Dependencies

> [com.Vonk.FusionJSON](com.Vonk.FusionJSON.md)  
## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.JSONFromFile.DragDrop/Config/DragDrop/Vonk vJSONFromFile DragDrop.fu?ref_type=heads">Config/DragDrop/Vonk vJSONFromFile DragDrop.fu</a></li>
</ul>
