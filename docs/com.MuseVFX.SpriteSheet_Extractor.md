# Sprite Sheet Extractor
___

## Category
Tools/Miscellaneous

## Author
Bryan Ray

## Version
1.0

___

## Description
<p>Sprite sheets are a common way of creating FX elements for video games. The entire animation is rendered to a single image in a grid pattern. The SpriteSheet_extractor fuse (just shows up as SpriteSheet at the moment because there is not currently a Sprite Sheet Creator) converts such an image into individual frames. The animation will loop continuously.

<p>The sprites must be <em>evenly spaced</em> and there should be no edge padding on the image in order to keep the sprite registered. By convention, the first frame is in the upper left corner, and the animation proceeds horizontally.

<h3>Controls</h3>
<p><strong>Columns / Rows:</strong> Count up how many sprites wide and tall your image is and enter the numbers here.

<p><strong>Start Frame:</strong> Determines which frame of your comp corresponds to the first frame of the sprite sheet animation.

<p><strong>Trim End:</strong> It is not uncommon for an animation to not entirely fill out a sprite sheet, leaving one or more empty frames in the last row. This control can be used to trim those empty frames off, allowing for a seamless loop.


___

## Download

Download a zipped atom package for offline installation:
> [com.MuseVFX.SpriteSheet_Extractor.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.MuseVFX.SpriteSheet_Extractor)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.MuseVFX.SpriteSheet_Extractor/Fuses/Miscellaneous/MT_SpriteSheet_Extractor.fuse?ref_type=heads">Fuses/Miscellaneous/MT_SpriteSheet_Extractor.fuse</a></li>
</ul>
