# Bake Animation
___

## Category
Scripts/Tool

## Author
Eyeon

## Version
3.2

___

## Description
<p>This tool script is used to 'bake' the animation of any animated control into a single value per frame. When run, a dialog listing all controls driven by a path, spline or modifier will appear. Select the control you want to bake, as well as the interval you want to use. An interval of 1 is default, representing one value per frame.</p>

<p>When you select OK, Fusion will obtain the value of that control at each frame, and apply it to a new path or polyline as appropriate. It will then replace the old animation or modifier applied to the control with the newly created path or spline.</p>

<p>You could use this script to convert the output of a Shake modifier to a path for hand tweaking, or to obtain an editable spline of the Unsteady size of a tracker....</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.wesuckless.BakeAnimation.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.wesuckless.BakeAnimation)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.BakeAnimation/Scripts/Tool/EyeonLegacy/Bake Animation.lua?ref_type=heads">Scripts/Tool/EyeonLegacy/Bake Animation.lua</a></li>
</ul>
