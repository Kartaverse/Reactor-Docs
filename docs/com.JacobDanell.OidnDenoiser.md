# Oidn Denoiser
___

## Category
Tools/Filter

## Author
Jacob Danell

## Version
1.1

___

## Description
<center><h2>Intel(R) Open Image Denoise (Oidn)</h2></center>
	Minimum = 16,

<p>TL:DR: Use this plugin to denoise your ray traced 3D renders using only the Beauty pass or together with an Albedo and a Normal pass for even better results.
<br>The AI is trained on ray traced renders (HDR and SDR) but also HDR lightmaps.</br></p>

<br></br>
<p>Intel Open Image Denoise is an open source library of high-performance, high-quality denoising filters for images rendered with ray tracing.</p>

<p>The purpose of Intel Open Image Denoise is to provide an open, high-quality, efficient, and easy-to-use denoising library that allows one to significantly reduce rendering times in ray tracing based rendering applications. It filters out the Monte Carlo noise inherent to stochastic ray tracing methods like path tracing, reducing the amount of necessary samples per pixel by even multiple orders of magnitude (depending on the desired closeness to the ground truth).</p>

<p>The filters can denoise images either using only the noisy color (beauty) buffer, or, to preserve as much detail as possible, can optionally utilize auxiliary feature buffers as well (e.g. albedo, normal). Such buffers are supported by most renderers as arbitrary output variables (AOVs) or can be usually implemented with little effort.</p>

<p>Intel Open Image Denoise supports Intel&reg; 64 architecture based CPUs and compatible architectures, and runs on anything from laptops, to workstations, to compute nodes in HPC systems. It is efficient enough to be suitable not only for offline rendering, but, depending on the hardware used, also for interactive ray tracing.
<br>A CPU with support for at least SSE4.1 is required to run Intel Open Image Denoise.</br></p>

<p>For more info, please check:</p>

<br>WSL thread: <a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?f=33&t=3998">https://www.steakunderwater.com/wesuckless/viewtopic.php?f=33&t=3998</a></br>
<br>Oidn webpage: <a href="https://openimagedenoise.github.io/">https://openimagedenoise.github.io/</a></br>


<p>Changelog:</p>

<br>v1.1, 2020-04-19</br>
<br>Fixed memory not being released after denoising</br>
<br>An error message will now show in the console telling you what went wrong.</br>
<br />
<br>v1.0, 2020-04-13:</br>
<br>First release! Running Oidn 1.2.</br>

___

## Download

Download a zipped atom package for offline installation:
> [com.JacobDanell.OidnDenoiser.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.JacobDanell.OidnDenoiser)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
</ul>

### macOS

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.JacobDanell.OidnDenoiser/Mac/Plugins/Oidn Denoiser/Oidn_Denoiser.plugin?ref_type=heads">Plugins/Oidn Denoiser/Oidn_Denoiser.plugin</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.JacobDanell.OidnDenoiser/Mac/Plugins/Oidn Denoiser/libOpenImageDenoise.0.dylib?ref_type=heads">Plugins/Oidn Denoiser/libOpenImageDenoise.0.dylib</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.JacobDanell.OidnDenoiser/Mac/Plugins/Oidn Denoiser/libtbb.dylib?ref_type=heads">Plugins/Oidn Denoiser/libtbb.dylib</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.JacobDanell.OidnDenoiser/Mac/Plugins/Oidn Denoiser/libtbbmalloc.dylib?ref_type=heads">Plugins/Oidn Denoiser/libtbbmalloc.dylib</a></li>

### Windows

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.JacobDanell.OidnDenoiser/Windows/Plugins/Oidn Denoiser/Oidn_Denoiser.plugin?ref_type=heads">Plugins/Oidn Denoiser/Oidn_Denoiser.plugin</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.JacobDanell.OidnDenoiser/Windows/Plugins/Oidn Denoiser/OpenImageDenoise.dll?ref_type=heads">Plugins/Oidn Denoiser/OpenImageDenoise.dll</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.JacobDanell.OidnDenoiser/Windows/Plugins/Oidn Denoiser/tbb.dll?ref_type=heads">Plugins/Oidn Denoiser/tbb.dll</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.JacobDanell.OidnDenoiser/Windows/Plugins/Oidn Denoiser/tbbmalloc.dll?ref_type=heads">Plugins/Oidn Denoiser/tbbmalloc.dll</a></li>
