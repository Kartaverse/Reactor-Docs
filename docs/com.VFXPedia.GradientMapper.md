# GradientMapper
___

## Category
Tools/Color

## Author
VFXPedia

## Version
1.0

___

## Description
<p>This macro gives Fusion the useful ability to map colours from a gradient to an image, based on the luminance of that image. Other channels may be used, and optionally, Perlin noise can be used to perturb the gradient being applied.</p>

<p>It is based on a Bitmap Mask to extract the luminance of the image. This can be softened, or its levels can be tweaked, or a different source channel can be used (e.g. RGB, hue or saturation). The resulting mask is then given to a FastNoise tool and used to modify the brightness of the Perlin noise it creates. By default, Noise Detail is set to 0 (flat) so no noise is generated, and the image's mask is used directly. FastNoise's various colour gradient controls can then be used to map colours to the mask.</p>

<p>Tip: In some cases, you might want to preserve the luminance of the original image while just replacing the colours. This can be easily done by using bright colours, then using a Channel Booleans tool to multiply the result of the GradientMapper with the Luminance of its source.</p>

<p>VFXPedia Page - Settings and Macros > GradientMapper Description:<br>
https://www.steakunderwater.com/VFXPedia/96.0.243.189/index0127.html?title=Settings_and_Macros/GradientMapper_Description</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.VFXPedia.GradientMapper.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.VFXPedia.GradientMapper)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.VFXPedia.GradientMapper/Macros/Color/GradientMapper.setting?ref_type=heads">Macros/Color/GradientMapper.setting</a></li>
</ul>
