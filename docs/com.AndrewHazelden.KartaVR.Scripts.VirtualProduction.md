# KartaVR Scripts | Virtual Production
___

## Category
Kartaverse/KartaVR/Scripts

## Author
Andrew Hazelden

## Version
5.75

___

## Description
<p>The KartaVR &quot;Virtual Production&quot; atom allows you optimize your on-set VFX workflows and interact with match moving department provided information like camera data, point clouds, and stand-in models. This is essential for effective scene integration and virtual produciton efforts in Fusion.

<p>The scripts in this atom package are the rare and exotic &quot;rosetta stone&quot; like tools that will allow your pipeline to interchange Fusion matchmoving data with external DCC apps, and make it a painless process to export PIXAR USD ASCII and Maya ASCII formatted copies of your Fusion 3D scene graph based nodes.</p>

<h2>Export Point Clouds</h2>

<p>The &quot;Export Point Cloud&quot; script is allows you to export XYZ ASCII (.xyz), PLY ASCII (.ply), PIXAR USD ASCII (.usda), Maya ASCII 2019 (.ma), and Maya MOVE ASCII (.mov) format.</p>

<p>PointCloud3D node based points or FBXMesh3D node OBJ mesh vertices can be exported to XYZ ASCII (.xyz), and PLY ASCII (.ply) formats. Camera3D nodes with per-frame Keyframe animated XYZ translation/rotation keys can be exported to the PIXAR USD ASCII (.usda), and Maya MOVE ASCII (.mov) format. Static (non-animated) Camera3D nodes can be exported to the Maya ASCII 2019 (.ma) format. Keyframe animated FBXMesh3D nodes with per-frame XYZ translation/rotation keys can be exported to the Maya MOVE ASCII (.mov) format. AlembicMesh3D nodes can be exported to the PIXAR USD ASCII (.usda), Maya ASCII 2019 (.ma), and Maya MOVE ASCII (.mov) format.</p>

<p>Note: <i>There is a &quot;KartaVR DragDrop&quot; atom package in Reactor that provides a matching .xyz point cloud importer functionality via dragging the .xyz file from your desktop folder into the Fusion/Resolve v16+ nodes views.</i></p>

<h2>For More Information About Camera Metadata</h2>

<p>If you would like find out how to extract the IMU metadata information from an video file, check out the Gyroflow toolset and its new motion data export options:<br>
<a href="http://gyroflow.xyz/">http://gyroflow.xyz/</a></p>


___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.KartaVR.Scripts.VirtualProduction.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/Time Editor/Clip Exports/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/Time Editor/Clip Exports/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/assets/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/assets/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/autosave/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/autosave/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/cache/bifrost/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/cache/bifrost/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/cache/nCache/fluid/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/cache/nCache/fluid/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/cache/particles/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/cache/particles/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/clips/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/clips/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/data/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/data/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/images/IMU-Track-Example.0001.png?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/images/IMU-Track-Example.0001.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/images/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/images/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/movies/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/movies/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/depth/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/depth/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furAttrMap/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furAttrMap/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furEqualMap/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furEqualMap/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furFiles/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furFiles/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furImages/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furImages/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furShadowMap/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furShadowMap/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/iprImages/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/iprImages/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sceneAssembly/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sceneAssembly/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/scenes/IMU-Track-Example.ma?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/scenes/IMU-Track-Example.ma</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/scripts/stub_folder.txt?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/scripts/stub_folder.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sound/gopro.wav?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sound/gopro.wav</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sourceimages/gopro-accl.csv?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sourceimages/gopro-accl.csv</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sourceimages/gopro-gyro.csv?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sourceimages/gopro-gyro.csv</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sourceimages/gopro.mp4?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sourceimages/gopro.mp4</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/workspace.mel?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/workspace.mel</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/movie/IMU-Track.mp4?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/movie/IMU-Track.mp4</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/scripts/IntertialTools.mel?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/scripts/IntertialTools.mel</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/scripts/gopro-accl.csv?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/scripts/gopro-accl.csv</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/scripts/gopro-gyro.csv?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/scripts/gopro-gyro.csv</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Bin/KartaVR/IMU-Tools-for-Maya/shelves/shelf_IMU_Tools.mel?ref_type=heads">Bin/KartaVR/IMU-Tools-for-Maya/shelves/shelf_IMU_Tools.mel</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Export Point Cloud.lua?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Export Point Cloud.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/IMU Tools.lua?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/IMU Tools.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/asterisk.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/asterisk.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/bbcode.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/bbcode.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/bold.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/bold.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/calendar.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/calendar.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/close.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/close.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/code.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/code.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/create.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/create.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/folder.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/folder.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/heading.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/heading.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/icons.zip?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/icons.zip</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/image.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/image.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/italic.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/italic.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/link.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/link.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/list.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/list.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/list_ordered.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/list_ordered.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/open.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/open.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/paragraph.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/paragraph.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/quit.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/quit.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/quote.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/quote.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/refresh.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/refresh.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/save.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/save.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/strike.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/strike.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/table.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/table.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/tint.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/tint.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/Images/underline.png?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/Images/underline.png</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Comp/KartaVR/Virtual Production/MadgwickAHRS.lua?ref_type=heads">Scripts/Comp/KartaVR/Virtual Production/MadgwickAHRS.lua</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.KartaVR.Scripts.VirtualProduction/Scripts/Tool/KartaVR/Virtual Production/Export Point Cloud.lua?ref_type=heads">Scripts/Tool/KartaVR/Virtual Production/Export Point Cloud.lua</a></li>
</ul>
