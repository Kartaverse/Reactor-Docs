# Reactor Atomz Expand
___

## Category
Scripts/Reactor

## Author
Andrew Hazelden

## Version
1.7

___

## Description
<p>The "Atomz Expand" script allows you to import zipped Reactor Atomz Packages by dragging them into the Fusion Nodes view from a desktop Explorer/Finder/Linux folder browsing window.</p>

<p>The DragDrop file supports dragging in multiple zip elements at the same time, and each item will be imported. This allows for easier NAS-based offline Reactor installation use.</p>

<p>You also have the option of importing Atomz package list files (atomz.lst). An atomz list text file works with an IFL image-file-list like document that is stored in the same folder as a collection of atomz zip files. The list is just a text file with a single package name per line that has the .lst file extension added to the filename. Using lst files let you define a custom selection list of packages to be installed at once. This technique can help with bootstrapping a local set of zipped offline usable Atomz packages in a bundle that get bulk loaded in fast.</p>

<h2>Requirements</h2>
<ul>
<li>Python v3.6 to v3.10 64-bit</li>
<li>Fusion Studio 16-19+ or Resolve 16-19+</li>
</ul>

<p>If you would like to provide feedback on the evolution of zipped Reactor Atomz Package workflows, please check out the <a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?t=6115">development thread on the Steakunderwater forum</a>.</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.AtomzExpand.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.AtomzExpand)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.AtomzExpand/Config/DragDrop/Atomz Expand DragDrop.fu?ref_type=heads">Config/DragDrop/Atomz Expand DragDrop.fu</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.AtomzExpand/Scripts/Comp/Atomz/Atomz Expand.py?ref_type=heads">Scripts/Comp/Atomz/Atomz Expand.py</a></li>
</ul>
