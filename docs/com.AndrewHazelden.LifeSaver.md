# LifeSaver
___

## Category
Tools/IO

## Author
Andrew Hazelden

## Version
2.2

___

## Description
<p>LifeSaver is a fuse based replacement for the traditional Saver or MediaOut nodes. This fuse uses EXRIO for the file output and supports multi-channel and multi-part EXR image saving. This node is special in that you can use the same node in comps that are created inside of both Resolve's Fusion page and inside of Fusion Standalone.</p>

<p>Fusion 9-18 or Resolve 15-18 is required.</p>

<p>Now includes customizable EXR compression format support.</p>

<h1>Usage</h1>

<p>Enter the filename for your image sequence into the Filename field.</p>

<p>The LifeSaver fuse allows you to save additional multi-part EXR image elements to the same EXR file using the following technique:</p>

<p>Step 1. Switch to the Channels tab and click the '+' button to add a new image input connection.</p>

<p>Step 2. In the Channels tab set new the 'Export Part #' ComboControl to 'Enabled', and update the 'Layer Name' so it is relevant.</p>

<p>Step 3. Connect your imagery to the new input connection on the fuse so it is written to the multi-part EXR output.</p>

<p>Step 4. You can use the fuse's 'Preview Input Connection' ComboControl to send a specific input image # to the Fuse's output connection. This makes it easier to work with a specific multi-part EXR exported image element further downstream in your flow, after the LifeSaver node</p>

<p>If you have added several extra node inputs to the LifeSaver fuse but have no images connected to them you should switch to the Channels tab and set the disconnected input's 'Export Part #' ComboControl menu to 'Disabled'</p>

<p>Note: Currently the EXR image format is the only supported output format in the LifeSaver fuse. In the future, it is (theoretically) possible to use the fuse based Clip() function to write out each of the individual flat image channels to disk using other image formats if that was a popular and frequently requested feature.</p>

<h1>Tokens</h1>

<p>LifeSaver supports the use of the following pre-defined token values in the Filename field. If any other value is written inside the ${} token format it will be looked up as if it was an environment variable.</p>

<pre>
${VERSION} - The LifeSaver node 'Version' field
${UUID} - The LifeSaver node 'UUID' field (f9fa311b-904c-4b93-892f-0d772887db88)
${COMP} - The current Fusion comp name (Composition1)
${COMPWIDTH} - The current comp default width (1920)
${COMPHEIGHT} - The current comp default height (1080)
${NODE} - The LifeSaver node name (LifeSaver1)
${FPS} - The current frame rate (24)
${FRAME} - The current unpadded frame number (1001)
${STARTFRAME} - The global start frame (1001)
${ENDFRAME} - The global end frame (1144)
${DURATION} - The global time duration (144)
${DATE} - The date in YYYY-MM-DD format (2018-06-16)
${TIME} - The time in HH.MM.SS format (14.59.05)
${HOME} - The Home folder name (/Users/andrew)
${USER} - The current user account name (andrew)
${HOSTNAME} - The computer's host name (Pine.local)
${SEP} - The file separator slash (/ or \)
${PLATFORM} - The OS Platform (Mac/Windows/Linux)
${FUHOST} - Is Fusion or Resolve the host package (Fusion/Resolve)
${FUVERSION} - The version of Fusion is running (9.02/15)
${UUID} - The per frame UUID value (f9fa311b-904c-4b93-892f-0d772887db88)
${SHELL1}-${SHELL4} - The Shell tokens textfield content is run in the Terminal/Command Prompt and the return value captured (echo Hello_World)
</pre>

<h2>Supported Frame Padding Indicators</h2>

<h3>${FRAME}</h3>

The current unpadded frame number (1001).

<h3>0000</h3>

The number you type in at the end of the filename before the file extension can be used as a frame padding indicator. The number of digits you add define how much padding is added. You can also type a number other then '0000' like '1001' and this value will be used along side the 'Sequence Offset' value on the node when you have the [x] Saver Relative Numbering checkbox enabled.

<h3>&#37;04d</h3>

The c-code style printf integer number formating symbol can be used to define the frame padding token.

<h3>####</h3>

The number sign/hash/octothorp # character can be used to define the frame padding (0000).


<h2>Filename Examples</h2>

<p>Filename Token Example 1:<br>
Comp:/${COMP}/${COMP}_${NODE}_${VERSION}.0000.exr</p>

<p>This would result in a rendered EXR image filename like:<br>
/Volumes/VFX/MultiChannel/MultiChannel_LifeSaver1_v001.0000.exr</p>

<p>Filename Token Example 2:<br>
Comp:/${COMP}/${COMP}_${NODE}.$06d.exr</p>

<p>This would result in a rendered EXR image filename like:<br>
/Volumes/VFX/MultiChannel/MultiChannel_LifeSaver1.000000.exr</p>

___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.LifeSaver.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.LifeSaver)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.LifeSaver/Config/IO/LifeSaver.fu?ref_type=heads">Config/IO/LifeSaver.fu</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.LifeSaver/Fuses/IO/LifeSaver.fuse?ref_type=heads">Fuses/IO/LifeSaver.fuse</a></li>
</ul>
