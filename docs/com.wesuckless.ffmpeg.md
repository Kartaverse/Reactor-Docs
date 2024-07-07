# FFmpeg
___

## Category
Bin

## Author
FFmpeg Dev

## Version
89994.0

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

## Download

Download a zipped atom package for offline installation:
> [com.wesuckless.ffmpeg.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.wesuckless.ffmpeg)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/README.txt?ref_type=heads">Bin/ffmpeg/README.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/bootstrap.min.css?ref_type=heads">Bin/ffmpeg/doc/bootstrap.min.css</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/default.css?ref_type=heads">Bin/ffmpeg/doc/default.css</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/developer.html?ref_type=heads">Bin/ffmpeg/doc/developer.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/faq.html?ref_type=heads">Bin/ffmpeg/doc/faq.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/fate.html?ref_type=heads">Bin/ffmpeg/doc/fate.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffmpeg-all.html?ref_type=heads">Bin/ffmpeg/doc/ffmpeg-all.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffmpeg-bitstream-filters.html?ref_type=heads">Bin/ffmpeg/doc/ffmpeg-bitstream-filters.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffmpeg-codecs.html?ref_type=heads">Bin/ffmpeg/doc/ffmpeg-codecs.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffmpeg-devices.html?ref_type=heads">Bin/ffmpeg/doc/ffmpeg-devices.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffmpeg-filters.html?ref_type=heads">Bin/ffmpeg/doc/ffmpeg-filters.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffmpeg-formats.html?ref_type=heads">Bin/ffmpeg/doc/ffmpeg-formats.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffmpeg-protocols.html?ref_type=heads">Bin/ffmpeg/doc/ffmpeg-protocols.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffmpeg-resampler.html?ref_type=heads">Bin/ffmpeg/doc/ffmpeg-resampler.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffmpeg-scaler.html?ref_type=heads">Bin/ffmpeg/doc/ffmpeg-scaler.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffmpeg-utils.html?ref_type=heads">Bin/ffmpeg/doc/ffmpeg-utils.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffmpeg.html?ref_type=heads">Bin/ffmpeg/doc/ffmpeg.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffplay-all.html?ref_type=heads">Bin/ffmpeg/doc/ffplay-all.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffplay.html?ref_type=heads">Bin/ffmpeg/doc/ffplay.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffprobe-all.html?ref_type=heads">Bin/ffmpeg/doc/ffprobe-all.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/ffprobe.html?ref_type=heads">Bin/ffmpeg/doc/ffprobe.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/general.html?ref_type=heads">Bin/ffmpeg/doc/general.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/git-howto.html?ref_type=heads">Bin/ffmpeg/doc/git-howto.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/libavcodec.html?ref_type=heads">Bin/ffmpeg/doc/libavcodec.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/libavdevice.html?ref_type=heads">Bin/ffmpeg/doc/libavdevice.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/libavfilter.html?ref_type=heads">Bin/ffmpeg/doc/libavfilter.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/libavformat.html?ref_type=heads">Bin/ffmpeg/doc/libavformat.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/libavutil.html?ref_type=heads">Bin/ffmpeg/doc/libavutil.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/libswresample.html?ref_type=heads">Bin/ffmpeg/doc/libswresample.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/libswscale.html?ref_type=heads">Bin/ffmpeg/doc/libswscale.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/mailing-list-faq.html?ref_type=heads">Bin/ffmpeg/doc/mailing-list-faq.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/nut.html?ref_type=heads">Bin/ffmpeg/doc/nut.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/platform.html?ref_type=heads">Bin/ffmpeg/doc/platform.html</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/doc/style.min.css?ref_type=heads">Bin/ffmpeg/doc/style.min.css</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/presets/ffprobe.xsd?ref_type=heads">Bin/ffmpeg/presets/ffprobe.xsd</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/presets/libvpx-1080p.ffpreset?ref_type=heads">Bin/ffmpeg/presets/libvpx-1080p.ffpreset</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/presets/libvpx-1080p50_60.ffpreset?ref_type=heads">Bin/ffmpeg/presets/libvpx-1080p50_60.ffpreset</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/presets/libvpx-360p.ffpreset?ref_type=heads">Bin/ffmpeg/presets/libvpx-360p.ffpreset</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/presets/libvpx-720p.ffpreset?ref_type=heads">Bin/ffmpeg/presets/libvpx-720p.ffpreset</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Bin/ffmpeg/presets/libvpx-720p50_60.ffpreset?ref_type=heads">Bin/ffmpeg/presets/libvpx-720p50_60.ffpreset</a></li>
</ul>

### Linux

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Linux/Bin/ffmpeg/LICENSE.txt?ref_type=heads">Bin/ffmpeg/LICENSE.txt</a></li>

### macOS

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Mac/Bin/ffmpeg/LICENSE.txt?ref_type=heads">Bin/ffmpeg/LICENSE.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Mac/Bin/ffmpeg/bin/ffmpeg?ref_type=heads">Bin/ffmpeg/bin/ffmpeg</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Mac/Bin/ffmpeg/bin/ffplay?ref_type=heads">Bin/ffmpeg/bin/ffplay</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Mac/Bin/ffmpeg/bin/ffprobe?ref_type=heads">Bin/ffmpeg/bin/ffprobe</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Mac/Bin/ffmpeg/bin/libavcodec.58.dylib?ref_type=heads">Bin/ffmpeg/bin/libavcodec.58.dylib</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Mac/Bin/ffmpeg/bin/libavdevice.58.dylib?ref_type=heads">Bin/ffmpeg/bin/libavdevice.58.dylib</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Mac/Bin/ffmpeg/bin/libavfilter.7.dylib?ref_type=heads">Bin/ffmpeg/bin/libavfilter.7.dylib</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Mac/Bin/ffmpeg/bin/libavformat.58.dylib?ref_type=heads">Bin/ffmpeg/bin/libavformat.58.dylib</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Mac/Bin/ffmpeg/bin/libavutil.56.dylib?ref_type=heads">Bin/ffmpeg/bin/libavutil.56.dylib</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Mac/Bin/ffmpeg/bin/libpostproc.55.dylib?ref_type=heads">Bin/ffmpeg/bin/libpostproc.55.dylib</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Mac/Bin/ffmpeg/bin/libswresample.3.dylib?ref_type=heads">Bin/ffmpeg/bin/libswresample.3.dylib</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Mac/Bin/ffmpeg/bin/libswscale.5.dylib?ref_type=heads">Bin/ffmpeg/bin/libswscale.5.dylib</a></li>

### Windows

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Windows/Bin/ffmpeg/LICENSE.txt?ref_type=heads">Bin/ffmpeg/LICENSE.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Windows/Bin/ffmpeg/bin/avcodec-58.dll?ref_type=heads">Bin/ffmpeg/bin/avcodec-58.dll</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Windows/Bin/ffmpeg/bin/avdevice-58.dll?ref_type=heads">Bin/ffmpeg/bin/avdevice-58.dll</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Windows/Bin/ffmpeg/bin/avfilter-7.dll?ref_type=heads">Bin/ffmpeg/bin/avfilter-7.dll</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Windows/Bin/ffmpeg/bin/avformat-58.dll?ref_type=heads">Bin/ffmpeg/bin/avformat-58.dll</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Windows/Bin/ffmpeg/bin/avutil-56.dll?ref_type=heads">Bin/ffmpeg/bin/avutil-56.dll</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Windows/Bin/ffmpeg/bin/ffmpeg.exe?ref_type=heads">Bin/ffmpeg/bin/ffmpeg.exe</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Windows/Bin/ffmpeg/bin/ffplay.exe?ref_type=heads">Bin/ffmpeg/bin/ffplay.exe</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Windows/Bin/ffmpeg/bin/ffprobe.exe?ref_type=heads">Bin/ffmpeg/bin/ffprobe.exe</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Windows/Bin/ffmpeg/bin/postproc-55.dll?ref_type=heads">Bin/ffmpeg/bin/postproc-55.dll</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Windows/Bin/ffmpeg/bin/swresample-3.dll?ref_type=heads">Bin/ffmpeg/bin/swresample-3.dll</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.ffmpeg/Windows/Bin/ffmpeg/bin/swscale-5.dll?ref_type=heads">Bin/ffmpeg/bin/swscale-5.dll</a></li>
