# Altus Denoiser Ultra
___

## Author
Andrew Hazelden

## Version
1.0

## Category
Legacy/Tools/Filter

___

## Description
<p>This fuse uses the Altus Denoiser CLI (command line interface) to reduce the noise in V-ray pathtracer rendered EXR imagery.</p>

<p>The Altus Denoiser CLI software is available for purchase on the Innobright website:<br>
https://www.innobright.com/about-altus/</p>

<p>The AltusDenoiserUltra fuse is compatible with Fusion 9.0.2. AltusDenoiserUltra requires the installation of the Reactor provided SwitchElse.fuse.</p>

<h2>Vray for Maya Render Channels</h2>

<p>In order to use thise fuse, Altus expects you to have rendered a pair of buffer 0 (b0) and buffer 1 (b1) images that have fixed noise sampling patterns enabled. By having the seed value for the fixed noise sampling set at two different settings for the b0 and b1 images, Altus is able to more accuratly target the multi-channel noise reduction where it is required.</p>

<p>Altus requires the following EXR image channels to be enabled in V-Ray's render settings:</p>

<ul>
	<li>rgb</li>
	<li>DiffuseFilter</li>
	<li>MatteShadow</li>
	<li>Reflection</li>
	<li>WorldNormals</li>
	<li>WorldPositions</li>
</ul>

<p>The fastest way to generate these render elements is to turn on the V-Ray "vrayRE_Denoiser" and "vrayRE_Matte_shadow" render elements.</p>



<h2>Vray for Maya Fixed Noise Sampling</h2>

<p>The Altus Buffer 0 Vray for Maya MEL setting is:</p>

<pre>
	setAttr "vraySettings.dmcs_timeDependent" 0;
	setAttr "vraySettings.dmcs_randomSeed" 0;"
</pre>


<p>The Altus Buffer 1 Vray for Maya MEL setting is:</p>

<pre>
	setAttr "vraySettings.dmcs_timeDependent" 0;
	setAttr "vraySettings.dmcs_randomSeed" 50000;"
</pre>



<h2>AltusDenoiserUltra Example Comp</h2>

<p>An example Fusion comp file can be found at the "Reactor:/Deploy/Comps/AltusDenoiser/AltusDenoiserUltra.comp" filepath. This example composite includes a pair of V-Ray rendered b0 and b1 EXR images that you can use to learn how Altus works and test the DoD cropping and filter settings.</p>



<h2>Macro Usage</h2>

<p>Step 1. Add the "AltusDenoiserUltra" macro to your comp. The macro's group is expanded by default so you can edit the settings.</p>

<p>Step 2. Relink your imagery into the b0 and b1 sets of Loaders on the far left side of the macro group's flow work area. If you are working with multi-part EXRs you can manually select which part you want to extract the image channels from manually on each of the loader nodes.</p>

<p>Step 3. Enable the HiQ rendering mode so the macro's embedded savers are able to interactivly render the individual multi-channel extracted exr image elements to the "Comp:/Media/altus_input" folder.</p>

<p>Step 4. Press the "Render" button to render an intial denoised output to the "Comp:/Media/altus_output" folder.<p>

<p>Step 5. Select the "AltusDenoiserUltra" macro and view its attributes in the Tools view. You can use the onscreen DoD crop handles to reduce the amount of processing Altus has to do down to a smaller cropped region.</p>

<p>Step 6. The "Output Mode" control lets you switch between viewing the original "Input Image", and the "Denoised Result". When the Output Mode is seto to "Input Image" you are able to use the "Buffer" ComboControl menu to switch between viewing B0 and B1. The "Channels" ComboControl menu lets you view each of the Altus formatted EXR image channels that were extracted from your V-Ray render elements.</p> 


<h2>Notes</h2>

<p>Altus is capable of denoising images from other production renderers like Mantra, Arnold, Maxwell Render, Mental Ray and RenderMan but it is outside the current focus and usage scope of this tool to try and implement support users of those renderers.</p>

<p>The "Processing Quality" should be set to the faster "Preview" setting when you are refining the settings. Once thinge are looking close to perfect you can switch the slower but cleaner "Production" setting to do a slightly better output quality. The &#91;x&#93; Firefly checkbox is useful for suppresing very small super bright artifacts that happen inside specular highlights in the rendered image.</p>

___

## Dependencies

> com.wesuckless.SwitchElse  
## Deploy

### Common (No Architecture)

> Comps/AltusDenoiser/AltusDenoiserUltra.comp  
> Comps/AltusDenoiser/Media/altus_input/DiffuseFilter_b0.0001.exr  
> Comps/AltusDenoiser/Media/altus_input/DiffuseFilter_b1.0001.exr  
> Comps/AltusDenoiser/Media/altus_input/MatteShadow_b0.0001.exr  
> Comps/AltusDenoiser/Media/altus_input/MatteShadow_b1.0001.exr  
> Comps/AltusDenoiser/Media/altus_input/Reflection_b0.0001.exr  
> Comps/AltusDenoiser/Media/altus_input/Reflection_b1.0001.exr  
> Comps/AltusDenoiser/Media/altus_input/WorldNormals_b0.0001.exr  
> Comps/AltusDenoiser/Media/altus_input/WorldNormals_b1.0001.exr  
> Comps/AltusDenoiser/Media/altus_input/WorldPositions_b0.0001.exr  
> Comps/AltusDenoiser/Media/altus_input/WorldPositions_b1.0001.exr  
> Comps/AltusDenoiser/Media/altus_input/rgb_b0.0001.exr  
> Comps/AltusDenoiser/Media/altus_input/rgb_b1.0001.exr  
> Comps/AltusDenoiser/Media/altus_output/altus.0001.log  
> Comps/AltusDenoiser/Media/satellite_lighting_b0.0001.exr  
> Comps/AltusDenoiser/Media/satellite_lighting_b1.0001.exr  
> Fuses/Filter/AltusDenoiserCore.fuse  
> Macros/Filter/AltusDenoiserUltra.setting  
