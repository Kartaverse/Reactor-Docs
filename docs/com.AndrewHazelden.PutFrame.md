# PutFrame
___

## Author
Andrew Hazelden

## Version
1.101

## Category
Legacy/Tools/IO

___

## Description
<p>PutFrame.fuse allows you to save RGBA channel based BMP/GIF/JPEG/PNG/TGA/TIFF/ imagery to disk using a pure fuse based approach which is cross-platform compatible. This is possible due to the use of the relatively new Fuse API's "Clip:PutFrame()" functionality.</p>

<h2>Why does this fuse exist?</h2>

<p>The "PutFrame.fuse" provided by this atom package, along with the "GetFrame.fuse" that is available separately in Reactor, can be used as a pair of learning tools should you need to re-create Saver node like approaches in your own fuses. The design idea of those two fuses is to enable Fusion based TDs to take on workflow tasks that need an interactive CLI (command-line) based "image pipe" equavalent to the built-in "RunCommand" node.</p>

<p>This concept is very powerful in that it makes it possible to create new fuses that could interactively push live image content from the Fusion node graph out to external CLI tools, and then automatically and seamlessly bring the resulting imagery back into the flow, on-the-fly, in a dynamic and unbroken, per-timeline frame based approach that would work equally well on Fusion Render Nodes and artist based Fusion GUI sessions.</p>

<p>If fuse writing TDs ever wanted to access external CLI based image denoiser libraries, OpenCV, Tensor AI/machine learning tools, hardware video I/O tools, NDI network frame sharing tools, Syphon, Imagemagick, FFmpeg, or anything else that takes an image input and generates an image output, you'd need this special GetFrame and PutFrame combo of techniques.</p>

<h2>Fusion/Resolve Requirements</h2>
	
<p>This fuse is compatible with Fusion Standalone 16+ and Resolve 16+.</p>

<p>Unfortunately, the "PutFrame.fuse" can't be used in Fusion 9 Standalone since the required Fuse API functionality did not exist yet.</p>

<h2>Email Andrew Hazelden</h2>
<p><a href="mailto:andrew@andrewhazelden.com">andrew@andrewhazelden.com</a></p>


___

## Dependencies

## Deploy

### Common (No Architecture)

> Fuses/IO/PutFrame.fuse  
