# NetLoader
___

## Category
Legacy/Tools/IO

## Author
Andrew Hazelden

## Version
1.3

___

## Description
<p>The NetLoader fuse uses cURL to download and display a still image in Fusion's viewer window using the "file://", "http://", and "https://" web protocols. To use this node type in a URL, and then click the "Download Image" button.</p>

<p>The NetLoader fuse allows you to load jpg/png/bmp/exr/fusepic/raw/tga/tiff/psd format imagery into the composite. In Fusion Standalone you can also load in mp4 and mov movies and scrubbing the timeline will update the current frame in the video. Since this Loader node replacement is implemented as a fuse you can instance this node in your comp, and you can save S1-S6 settings.</p>

<p>Fusion 9.0.2 or Resolve 15-16 is required.</p>

<p>If there is an error loading an image you will see a blank canvas. The "Verbose" button lets you see the raw cURL download data which is useful for troubleshooting HTTP error messages.</p>

<p>If you have auto-proxy enabled (APrx) in your comp you may notice a view updating glitch occasionally down stream of this fuse related to the way the proxy resolution is set. If this bothers you, adding a crop node after this fuse, and setting the crop node to the frame size should stop this glitch from happening.</p>


<h1>GUI Controls</h1>


<h2>URL (TextEditControl)</h2>

<p>The URL field allows you to download images using a cURL HTTP/HTTPS network connection.</p>


<h2>File Type (ComboControl)</h2>

<p>Lets you define the file type of the Download.</p>

<ul>
<li>JPEG</li>
<li>PNG</li>
<li>BMP</li>
<li>EXR</li>
<li>FUSEPIC</li>
<li>RAW</li>
<li>TGA</li>
<li>TIFF</li>
<li>PSD</li>
<li>MP4</li>
<li>MOV</li>
</ul>


<h2>Download Image (Button)</h2>

<p>Clicking this button will refresh the image in the view by downloading the image that is defined in the URL field.</p>


<h2>Open Containing Folder (Button)</h2>

<p>Clicking this button will show a desktop folder browsing window that shows the temporary folder where NetLoader images are saved to.</p>


<h2>Clear Old Downloads (Button)</h2>

<p>Should a previous download be removed automatically the next time the comp is opened, or when a new node of the same name is added to the comp?</p>


<h2>Verbose (Checkbox)</h2>

<p>Print debugging information like the raw cURL download data.</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.NetLoader.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.NetLoader)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.NetLoader/Fuses/IO/NetLoader.fuse?ref_type=heads">Fuses/IO/NetLoader.fuse</a></li>
</ul>
