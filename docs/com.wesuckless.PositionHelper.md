# Position Helper Fuse
___

## Category
Modifiers

## Author
Stefan Ihringer

## Version
1.1

___

## Description
<p>A modifier to scale, smooth or change the reference frame of a 2D path.<p>The reference frame is defined as the time where the path is equal to Fusion's null position for transformation offsets (0.5/0.5). The tracker doesn't make it easy to pick an arbitrary reference frame and the Locator3D doesn't provide this option at all. Without this Fuse you need to modify a path with an Offset modifier and type in appropriate numbers.</p>

<p>With PositionHelper you can just pick a reference frame (defaults to current one) and you're done. When the track has been created for a different resolution than the image that is to be transformed, you can use this modifier to do the conversion for you. The filtering option allows you to average the keyframes of a path and to calculate the jitter component (original minus smoothed path).</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.wesuckless.PositionHelper.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.wesuckless.PositionHelper)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.PositionHelper/Fuses/Modifiers/PositionHelper.fuse?ref_type=heads">Fuses/Modifiers/PositionHelper.fuse</a></li>
</ul>
