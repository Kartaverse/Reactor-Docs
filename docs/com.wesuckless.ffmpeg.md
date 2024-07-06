# FFmpeg
___

## Author
 : FFmpeg Dev

## Version
 : v89994.0

## Category
 : Bin
___

## Description
<p>FFmpeg is the leading multimedia framework, able to decode, encode, transcode, mux, demux, stream, filter and play pretty much anything that humans and machines have created. It supports the most obscure ancient formats up to the cutting edge. No matter if they were designed by some standards committee, the community or a corporation.</p>

<h2>Open Source License:</h2>
<p>GNU LPGL 2.1 + GPL v2<br>
The FFmpeg Shared Linking 64-bit for Windows/MacOS atom was packaged by Andrew Hazelden.</p>
<p>Note: This atom only includes Windows and MacOS builds of FFmpeg.</p>


<h2>For More Information:</h2>
<p>https://ffmpeg.org/</p>

<h3>MacOS Tip</h3>
<p>If you are on MacOS you need to adjust the MacOS permissions for FFmpeg using the following Lua command in the Fusion Console tab:</p>

<pre>
	-- Set the FFmpeg program on MacOS to have executable permissions so the ffmpeg command line tool can be used:
	command = 'chmod -R 755 "' .. app:MapPath('Reactor:/Deploy/Bin/ffmpeg/bin/') .. '"'
	print("[Permissions Update] " .. command)
	os.execute(command)
</pre>


<h3>Linux Tip</h3>
Linux users need to install their own version of ffmpeg using a native Linux package manager. You can check the current installation location of ffmpeg using the terminal command "which ffmpeg".

<p>CentOS Install:</p>

<pre>
sudo yum -y install ffmpeg
</pre>

<p>Ubuntu Install:</p>

<pre>
sudo add-apt-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get -y install ffmpeg
</pre>

<p>Arch Linux / Manjaro Linux Install:</p>

<pre>
sudo pacman -S ffmpeg
</pre>
___

## Dependencies


___

## Deploy

### Common (No Architecture)

> Bin/ffmpeg/README.txt  
> Bin/ffmpeg/doc/bootstrap.min.css  
> Bin/ffmpeg/doc/default.css  
> Bin/ffmpeg/doc/developer.html  
> Bin/ffmpeg/doc/faq.html  
> Bin/ffmpeg/doc/fate.html  
> Bin/ffmpeg/doc/ffmpeg-all.html  
> Bin/ffmpeg/doc/ffmpeg-bitstream-filters.html  
> Bin/ffmpeg/doc/ffmpeg-codecs.html  
> Bin/ffmpeg/doc/ffmpeg-devices.html  
> Bin/ffmpeg/doc/ffmpeg-filters.html  
> Bin/ffmpeg/doc/ffmpeg-formats.html  
> Bin/ffmpeg/doc/ffmpeg-protocols.html  
> Bin/ffmpeg/doc/ffmpeg-resampler.html  
> Bin/ffmpeg/doc/ffmpeg-scaler.html  
> Bin/ffmpeg/doc/ffmpeg-utils.html  
> Bin/ffmpeg/doc/ffmpeg.html  
> Bin/ffmpeg/doc/ffplay-all.html  
> Bin/ffmpeg/doc/ffplay.html  
> Bin/ffmpeg/doc/ffprobe-all.html  
> Bin/ffmpeg/doc/ffprobe.html  
> Bin/ffmpeg/doc/general.html  
> Bin/ffmpeg/doc/git-howto.html  
> Bin/ffmpeg/doc/libavcodec.html  
> Bin/ffmpeg/doc/libavdevice.html  
> Bin/ffmpeg/doc/libavfilter.html  
> Bin/ffmpeg/doc/libavformat.html  
> Bin/ffmpeg/doc/libavutil.html  
> Bin/ffmpeg/doc/libswresample.html  
> Bin/ffmpeg/doc/libswscale.html  
> Bin/ffmpeg/doc/mailing-list-faq.html  
> Bin/ffmpeg/doc/nut.html  
> Bin/ffmpeg/doc/platform.html  
> Bin/ffmpeg/doc/style.min.css  
> Bin/ffmpeg/presets/ffprobe.xsd  
> Bin/ffmpeg/presets/libvpx-1080p.ffpreset  
> Bin/ffmpeg/presets/libvpx-1080p50_60.ffpreset  
> Bin/ffmpeg/presets/libvpx-360p.ffpreset  
> Bin/ffmpeg/presets/libvpx-720p.ffpreset  
> Bin/ffmpeg/presets/libvpx-720p50_60.ffpreset  

### macOS

> Bin/ffmpeg/LICENSE.txt  
> Bin/ffmpeg/bin/ffmpeg  
> Bin/ffmpeg/bin/ffplay  
> Bin/ffmpeg/bin/ffprobe  
> Bin/ffmpeg/bin/libavcodec.58.dylib  
> Bin/ffmpeg/bin/libavdevice.58.dylib  
> Bin/ffmpeg/bin/libavfilter.7.dylib  
> Bin/ffmpeg/bin/libavformat.58.dylib  
> Bin/ffmpeg/bin/libavutil.56.dylib  
> Bin/ffmpeg/bin/libpostproc.55.dylib  
> Bin/ffmpeg/bin/libswresample.3.dylib  
> Bin/ffmpeg/bin/libswscale.5.dylib  
