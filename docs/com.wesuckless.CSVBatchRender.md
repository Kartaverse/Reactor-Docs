# CSV Batch Render
___

## Category
Scripts/Comp

## Author
Eyeon

## Version
1.0

___

## Description
<p>Changes the tools of a comp based on a CSV file and renders the comps via the Fusion Studio Render Manager.</p>

<p>The header/first line of the CSV file should list each of the Tools and the inputs.</p>

<p>CSV Header Row Example:<br>
MainTitle,MainTitle2,MainTitle3.Text</p>

<p>This results in MainTitle.StyledText, MainTitle2.StyledText and MainTitle3.Text
being replaced with with proper text from the data below.</p>

<p>You can access a Saver node's Filename input with either "Saver.Clip" or "Saver.Filename" with a CSV like:</p>

<p>Text1.StyledText,Saver1.Filename<br>
Episode 1,Comp:/Renders/Title1.mov</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.wesuckless.CSVBatchRender.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.wesuckless.CSVBatchRender)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.wesuckless.CSVBatchRender/Scripts/Comp/EyeonLegacy/CSV Batch Render.lua?ref_type=heads">Scripts/Comp/EyeonLegacy/CSV Batch Render.lua</a></li>
</ul>
