# KartaVR Scripts | Movies
___

## Author
 : Andrew Hazelden

## Version
 : v5.73

## Category
 : Kartaverse/KartaVR/Scripts
___

## Description
<p>The KartaVR Movies collection of scripts provide tools for capturing video, extracing image sequences, and merging stereo video clips.</p>

<h2>Video Snapshot</h2>

<p>The "Video Snapshot" script allows you to capture video into Fusion/Resolve's Fusion page from a live video input source such as an HDMI/SDI/USB/Thunderbolt video device via Windows DirectShow or macOS AV Foundation libraries. After you capture the footage, your media can be added to the active comp by clicking the "Add Loader node" button. If you are saving your captured footage to the "Comp:/" PathMap location in the Video Snapshot settings, make sure you actually saved the .comp file to disk *first* so the relative PathMap is resovled correctly. Clicking the "?" button in the Video Snapshot window will display a built-in HTML help document in a window.</p> 

<h2>Combine Stereo Movies</h2>
<p>The "Combine Stereo Movies" script allows you to merge separate left and right eye view stereo movies into over/under, and side by side stereo formats. You can do this with H.264, H.265, and PreRes videos. Internally the script uses the open-source FFmpeg command-line program which is installed using the Reactor "Bin" category provided atom package.</p>

<h2>Convert Movies to Image Sequences</h2>
<p>The "Convert Movies to Image Sequences" script allows you to batch convert a folder of movie files into individually named image sequences and extracted audio files. This is handy if you want to work reliable in Fusion with a series of Loader nodes (and image sequences) in your composite but the project you are doing has provided you with a large folder of MP4/ProRes clips you need to transcode.</p>

<p>This script is an integral tool if you want to work with video sourced media in a PTGui Pro based 360VR pipeline. The workflow combination of the "Convert Movies to Image Sequences" script, KartaVR's "Batch Builder Extractor/Creator" scripts, and PTGui Pro's Batch Builder tool can be an effective and affordable way to stitch 360VR footage coming from fisheye or rectilinear image projections, without falling into the typical trap of having to pay for high-cost, subscription only, 360VR video stitching tools...</p>
___

## Dependencies

> com.wesuckless.ffmpeg  

___

## Deploy

### Common (No Architecture)

> Bin/KartaVR/FFMPEG Encoding Intool Script/FFMPEG Encode Intool End Render Script.lua  
> Bin/KartaVR/FFMPEG Encoding Intool Script/FFMPEG Encoding Saver Intool Script.comp  
> Scripts/Comp/KartaVR/Movies/Combine Stereo Movies.lua  
> Scripts/Comp/KartaVR/Movies/Convert Movies to Image Sequences.lua  
> Scripts/Comp/KartaVR/Movies/Video Snapshot.lua  
