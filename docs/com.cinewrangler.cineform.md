# CineForm Loader/Saver
___

## Author
Olaf Matthes

## Version
1.5

## Category
Tools/IO

___

## Description
<p>The <b>CineForm Loader/Saver</b> is a free (as in beer) loader and saver for CineForm compressed DPX files (aka. DPX-C) and CineForm encoded QuickTime movies.</p>

<p>The plugin allows to load and save 10bit YUV 4:2:2, 12bit RGB(A) and 12bit Bayer RAW files (load only) and supports all CineForm compression settings. Additionally it provides view selection (both, left or right) for Stereo 3D CineForm files.<br />
The DPX-C format is basically a DPX file containing an 1/8 size thumbnail image as 10bit RGB data. Hidden to normal DPX file readers it contains the CineForm data for the full-size image. Since it is a single-frame format, it can also be used on renderfarms.</p>

<p><b>NOTE:</b> <i>After installing this plugin Fusion will default to the CineForm saver for DPX and QuickTime when you create a new saver and just specify the filename with the corresponding extension. To save to regular DPX or QuickTime files (using Fusion's internal savers) you need to specify that format in the file format list.</i></p>

<p>Latest version, some additional information and other Fusion stuff might be found at:<br />
<a href="http://www.cinewrangler.com/blackmagic-fusion-plugins/">http://www.cinewrangler.com/blackmagic-fusion-plugins/</a></p>
<p>&nbsp;</p>

<h3>License</h3>

<p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, <br />
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES <br />
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND <br />
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT <br />
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, <br />
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING <br />
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR <br />
OTHER DEALINGS IN THE SOFTWARE.
</p>
<p>&nbsp;</p>

<h3>Library Disclaimer</h3>

<p>This software uses free libraries provided by third-party organizations.<br />
The libraries are in detail:</p>

<p>1. CineForm video codec SDK by GoPro, Inc.<br />
<a href="https://gopro.github.io/cineform-sdk/">https://gopro.github.io/cineform-sdk/</a></p>

<p>Copyright 2017 GoPro, Inc.</p>

<p>Permission is hereby granted, free of charge, to any person obtaining a <br />
copy of this software and associated documentation files (the "Software"), <br />
to deal in the Software without restriction, including without limitation <br />
the rights to use, copy, modify, merge, publish, distribute, sublicense, <br />
and/or sell copies of the Software, and to permit persons to whom the <br />
Software is furnished to do so, subject to the following conditions:</p>

<p>The above copyright notice and this permission notice shall be included <br />
in all copies or substantial portions of the Software.</p>

<p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS <br />
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, <br />
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL <br />
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER <br />
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING <br />
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER <br />
DEALINGS IN THE SOFTWARE.</p>


___

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
</ul>

### Linux

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.cinewrangler.cineform/Linux/Plugins/Cinewrangler_CineForm.plugin?ref_type=heads">Plugins/Cinewrangler_CineForm.plugin</a></li>

### macOS

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.cinewrangler.cineform/Mac/Plugins/Cinewrangler_CineForm.plugin?ref_type=heads">Plugins/Cinewrangler_CineForm.plugin</a></li>

### Windows

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.cinewrangler.cineform/Windows/Plugins/Cinewrangler_CineForm.plugin?ref_type=heads">Plugins/Cinewrangler_CineForm.plugin</a></li>
