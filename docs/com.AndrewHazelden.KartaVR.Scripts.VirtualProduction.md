# KartaVR Scripts | Virtual Production
___

## Author
Andrew Hazelden

## Version
5.73

## Category
Kartaverse/KartaVR/Scripts

___

## Description
<p>The KartaVR &quot;Virtual Production&quot; atom allows you optimize your on-set VFX workflows and interact with match moving department provided information like camera data, point clouds, and stand-in models. This is essential for effective scene integration and virtual produciton efforts in Fusion.

<p>The scripts in this atom package are the rare and exotic &quot;rosetta stone&quot; like tools that will allow your pipeline to interchange Fusion matchmoving data with external DCC apps, and make it a painless process to export PIXAR USD ASCII and Maya ASCII formatted copies of your Fusion 3D scene graph based nodes.</p>
	
<h2>Export Point Clouds</h2>

<p>The &quot;Export Point Cloud&quot; script is an alpha grade tool that allows you to export XYZ ASCII (.xyz), PLY ASCII (.ply), PIXAR USD ASCII (.usda), Maya ASCII 2019 (.ma), and Maya MOVE ASCII (.mov) format.</p>

<p>PointCloud3D node based points or FBXMesh3D node OBJ mesh vertices can be exported to XYZ ASCII (.xyz), and PLY ASCII (.ply) formats. Camera3D nodes with per-frame Keyframe animated XYZ translation/rotation keys can be exported to the PIXAR USD ASCII (.usda), and Maya MOVE ASCII (.mov) format. Static (non-animated) Camera3D nodes can be exported to the Maya ASCII 2019 (.ma) format. Keyframe animated FBXMesh3D nodes with per-frame XYZ translation/rotation keys can be exported to the Maya MOVE ASCII (.mov) format. AlembicMesh3D nodes can be exported to the PIXAR USD ASCII (.usda), Maya ASCII 2019 (.ma), and Maya MOVE ASCII (.mov) format.</p>

<p>Note: <i>There is a &quot;KartaVR DragDrop&quot; atom package in Reactor that provides a matching .xyz point cloud importer functionality via dragging the .xyz file from your desktop folder into the Fusion/Resolve v16+ nodes views.</i></p>

<h2>For More Information About Camera Metadata</h2>

<p>If you would like find out how to extract the IMU metadata information from an video file, check out the Gyroflow toolset and its new motion data export options:<br>
<a href="http://gyroflow.xyz/">http://gyroflow.xyz/</a></p>



___

## Dependencies

## Deploy

### Common (No Architecture)

> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/Time Editor/Clip Exports/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/assets/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/autosave/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/cache/bifrost/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/cache/nCache/fluid/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/cache/particles/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/clips/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/data/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/images/IMU-Track-Example.0001.png  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/images/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/movies/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/depth/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furAttrMap/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furEqualMap/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furFiles/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furImages/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/fur/furShadowMap/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/renderData/iprImages/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sceneAssembly/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/scenes/IMU-Track-Example.ma  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/scripts/stub_folder.txt  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sound/gopro.wav  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sourceimages/gopro-accl.csv  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sourceimages/gopro-gyro.csv  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/sourceimages/gopro.mp4  
> Bin/KartaVR/IMU-Tools-for-Maya/example/IMU-Track-Maya-Project/workspace.mel  
> Bin/KartaVR/IMU-Tools-for-Maya/movie/IMU-Track.mp4  
> Bin/KartaVR/IMU-Tools-for-Maya/scripts/IntertialTools.mel  
> Bin/KartaVR/IMU-Tools-for-Maya/scripts/gopro-accl.csv  
> Bin/KartaVR/IMU-Tools-for-Maya/scripts/gopro-gyro.csv  
> Bin/KartaVR/IMU-Tools-for-Maya/shelves/shelf_IMU_Tools.mel  
> Scripts/Comp/KartaVR/Virtual Production/Export Point Cloud.lua  
> Scripts/Comp/KartaVR/Virtual Production/IMU Tools.lua  
> Scripts/Comp/KartaVR/Virtual Production/Images/asterisk.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/bbcode.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/bold.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/calendar.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/close.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/code.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/create.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/folder.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/heading.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/icons.zip  
> Scripts/Comp/KartaVR/Virtual Production/Images/image.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/italic.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/link.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/list.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/list_ordered.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/open.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/paragraph.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/quit.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/quote.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/refresh.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/save.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/strike.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/table.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/tint.png  
> Scripts/Comp/KartaVR/Virtual Production/Images/underline.png  
> Scripts/Comp/KartaVR/Virtual Production/MadgwickAHRS.lua  
> Scripts/Tool/KartaVR/Virtual Production/Export Point Cloud.lua  
