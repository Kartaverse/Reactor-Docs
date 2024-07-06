# GetFrame
___

## Author
 : Andrew Hazelden

## Version
 : v1.01

## Category
 : Legacy/Tools/IO
___

## Description
<p>GetFrame.fuse allows you to load RGBA channel based BMP/GIF/JPEG/PNG/TGA/TIFF/ imagery from a filepath on disk using the Fuse API's Clip:GetFrame() functionality. This fuse can be used as a learning tool should you need to re-create Loader node like approaches in your own fuses. The source code is kept to an absolute minimum to make this fuse easier to re-integrate into your own custom fuse based tools.</p>
	
<p>The Filename control supports the use of PathMaps.</p>

<h2>Why does this fuse exist?</h2>

<p>The "GetFrame.fuse" provided by this atom package, along with the "PutFrame.fuse" that is available separately in Reactor, can be used as a pair of learning tools should you need to re-create Saver node like approaches in your own fuses. The design idea of those two fuses is to enable Fusion based TDs to take on workflow tasks that need an interactive CLI (command-line) based "image pipe" equavalent to the built-in "RunCommand" node.</p>

<p>This concept is very powerful in that it makes it possible to create new fuses that could interactively push live image content from the Fusion node graph out to external CLI tools, and then automatically and seamlessly bring the resulting imagery back into the flow, on-the-fly, in a dynamic and unbroken, per-timeline frame based approach that would work equally well on Fusion Render Nodes and artist based Fusion GUI sessions.</p>

<p>If fuse writing TDs ever wanted to access external CLI based image denoiser libraries, OpenCV, Tensor AI/machine learning tools, hardware video I/O tools, NDI network frame sharing tools, Syphon, imagemagick, ffmpeg, or anything else that takes an image input and generates an image output, you'd need this special GetFrame and PutFrame combo of techniques.</p>


<h2>Fusion/Resolve Requirements</h2>

<p>This fuse is compatible with the 2D compositing nodes in Fusion Standalone v9-16.1 and Resolve v15-16.1.</p>

<h2>Email Andrew Hazelden</h2>
<p><a href="mailto:andrew@andrewhazelden.com">andrew@andrewhazelden.com</a></p>
___

## Dependencies


___

## Deploy

### Common (No Architecture)

> Fuses/IO/GetFrame.fuse  
