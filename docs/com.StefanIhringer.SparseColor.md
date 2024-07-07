# Sparse Color Fuse
___

## Category
Tools/Creator

## Author
Stefan Ihringer

## Version
1.1

___

## Description
<p>This fuse creates an interpolated gradient between one or multiple color seed points. In a simple use case, this can be thought of a four-corner gradient where the points are not fixed at the image corners. It has many more uses.

	<p>For example, you could use the Sparse Color Fuse to create a sky gradient based on multiple known colors from a plate. You can also use it to match a matte painting to the lighting changes of a shot, where a single color correction won't suffice (imagine that the left and right part of the shot are affected by various flickering light sources).</p>

	<p>There are up to 4 points that can be defined. If the interpolation is set to "Inverse Distance", however, you can create gradients with many more points by chaining SparseColor tools. Just check the "Store Metadata" checkbox, and this Fuse will save its seed points to the image's metadata table. In a downstream SparseColor tool, check the "Use Metadata" (enabled by default) to include these points in the gradient calculation.</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.StefanIhringer.SparseColor.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.StefanIhringer.SparseColor)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.StefanIhringer.SparseColor/Fuses/Creator/SparseColor.fuse?ref_type=heads">Fuses/Creator/SparseColor.fuse</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.StefanIhringer.SparseColor/Fuses/Creator/SparseColor.cl?ref_type=heads">Fuses/Creator/SparseColor.cl</a></li>
</ul>
