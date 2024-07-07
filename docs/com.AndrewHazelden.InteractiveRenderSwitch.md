# Interactive Render Switch Fuse
___

## Category
Tools/Flow

## Author
Andrew Hazelden

## Version
1.01

___

## Description
<p>The "InteractiveRenderSwitch.fuse" toggles the image output stream between an "Interactive" image input, or a "BatchRender" image input. The interactive vs batch rendering input switching is toggled automatically by Fusion so you can have different content processed and displayed in your flow during an artist driven interactive GUI session vs when a batch rendering mode is happening inside Fusion/Fusion Render Node.</p

<p>This fuse was inspired "Switch.fuse" by Stefan Ihringer.</p>

<p>Note: You might have to purge the active Fusion RAM cache for the entire comp timeline before the "Interactive Render Switch" fuse's output is truly swapped between interactive and batch mode. Automatic and seamless solutions to perform the timeline based RAM cache clearing are still being researched.</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.InteractiveRenderSwitch.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.InteractiveRenderSwitch)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.InteractiveRenderSwitch/Comps/Flow/InteractiveRenderSwitch.comp?ref_type=heads">Comps/Flow/InteractiveRenderSwitch.comp</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.InteractiveRenderSwitch/Fuses/Flow/InteractiveRenderSwitch.fuse?ref_type=heads">Fuses/Flow/InteractiveRenderSwitch.fuse</a></li>
</ul>
