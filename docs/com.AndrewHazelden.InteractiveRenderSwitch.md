# Interactive Render Switch Fuse
___

## Author
 : Andrew Hazelden

## Version
 : v1.01

## Category
 : Tools/Flow
___

## Description
<p>The "InteractiveRenderSwitch.fuse" toggles the image output stream between an "Interactive" image input, or a "BatchRender" image input. The interactive vs batch rendering input switching is toggled automatically by Fusion so you can have different content processed and displayed in your flow during an artist driven interactive GUI session vs when a batch rendering mode is happening inside Fusion/Fusion Render Node.</p
	
<p>This fuse was inspired "Switch.fuse" by Stefan Ihringer.</p>
	
<p>Note: You might have to purge the active Fusion RAM cache for the entire comp timeline before the "Interactive Render Switch" fuse's output is truly swapped between interactive and batch mode. Automatic and seamless solutions to perform the timeline based RAM cache clearing are still being researched.</p>
___

## Dependencies


___

## Deploy

### Common (No Architecture)

> Comps/Flow/InteractiveRenderSwitch.comp  
> Fuses/Flow/InteractiveRenderSwitch.fuse  
