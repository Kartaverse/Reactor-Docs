# Sqlite3
___

## Category
Bin/Dev

## Author
Andrew Hazelden

## Version
3.23

___

## Description
<p>This atom provides Sqlite3 for Windows. Sqlite3 is a cross-platform command line based database engine that is open source with a public domain license. Sqlite3 can be accessed from Lua using os.execute(), and from a Python script in Fusion.</p>

<p>It is possible to use Sqlite3 wrapper scripts for Lua and Python that can make it easier to use as part of a regular scripted workflow.

<h2>Sqlite3 Project</h2>
<p>https://sqlite.org/</p>

<h2>Sqlite3 Dccumentation</h2>
<p>http://sqlite.org/docs.html</p>

<h2>Sqlite3 Manual Installation</h2>

<h3>Windows Manual Install</h3>
<p>You can manually download Sqlite3 from the "Precompiled Binaries for Windows" section:<br>
http://sqlite.org/download.html</p>

<h3>macOS Manual Install</h3>
<p>Sqlite3 comes pre-installed with macOS.</p>

<h3>Linux Manual Install</h3>
<p>Linux users can install Sqlite3 using yum, apt-get, or pacman.</p>

<h4>Ubuntu Manual Install</h4>
<pre>sudo apt-get install sqlite3 libsqlite3-dev</pre>

<h2>Sqlite3 Usage Examples</h2>
<p>These macOS based examples show how Sqlite3 can be used from a BASH command prompt to open Resolve Project.db files. When you are researching new SQL commands it is helpful to have the ".header on" and ".mode column" tags added so you can get an idea of the data structure visually. Once you know the final search query to use you can remove those arguments from your queries to simplify the output.<p>

<p>Example 1 - List the Resolve Project Name and Timeline Video Clips</p>

<pre>sqlite3 "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Resolve Disk Database/Resolve Projects/Users/guest/Projects/Ozo Stitch/Project.db" ".header on" ".mode column" "SELECT ProjectName FROM SM_Project;" "SELECT Name, MediaFilePath, Start, Duration FROM Sm2TiItem WHERE DbType = 'Sm2TiVideoClip';"</pre>

<p>Example 1 Output:</p>
<pre>
ProjectName
-----------
Ozo Stitch

Name        MediaFilePath                                             Start       Duration
----------  --------------------------------------------------------  ----------  ----------
cam8.mp4    /Production/VFX/Resolve/Nokia Ozo+ Video Stitch/cam8.mp4  86400       268
</pre>

<p>Example 2 - List the Resolve Media Pool Video Clips</p>

<pre>sqlite3 "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Resolve Disk Database/Resolve Projects/Users/guest/Projects/Ozo Stitch/Project.db" ".header on" ".mode column" "SELECT Name, DbType, UniqueMediaPoolItemId FROM Sm2MPMedia WHERE DbType = 'Sm2MpVideoClip';"</pre>

<p>Example 2 Output:</p>

<pre>
Name        DbType          UniqueMediaPoolItemId
----------  --------------  ------------------------------------
cam3.mp4    Sm2MpVideoClip  2027c029-5a32-48be-9d94-9665090c37a5
cam6.mp4    Sm2MpVideoClip  c8017708-2d00-4a65-90dd-e33cd0408e88
cam2.mp4    Sm2MpVideoClip  fac1bcac-4fb7-4ca4-8e1d-2407bddf74f5
cam7.mp4    Sm2MpVideoClip  c2596427-2bd3-4ab5-996c-b97d3db93942
cam8.mp4    Sm2MpVideoClip  ad9b2904-c5a9-4e3a-a579-b8f5c3998c50
cam5.mp4    Sm2MpVideoClip  2d18b9c7-f1f1-4bae-b3e5-8dcbe6cc1d65
cam1.mp4    Sm2MpVideoClip  2d002633-2e23-4169-a938-d7291f7c15c3
cam4.mp4    Sm2MpVideoClip  97841817-6456-4784-9362-7455e835197b
</pre>

___

## Download

Download a zipped atom package for offline installation:
> [com.AndrewHazelden.Sqlite3.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.AndrewHazelden.Sqlite3)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
</ul>

### Linux

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.Sqlite3/Linux/Bin/sqlite3/LICENSE.txt?ref_type=heads">Bin/sqlite3/LICENSE.txt</a></li>

### macOS

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.Sqlite3/Mac/Bin/sqlite3/LICENSE.txt?ref_type=heads">Bin/sqlite3/LICENSE.txt</a></li>

### Windows

<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.Sqlite3/Windows/Bin/sqlite3/LICENSE.txt?ref_type=heads">Bin/sqlite3/LICENSE.txt</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.Sqlite3/Windows/Bin/sqlite3/sqldiff.exe?ref_type=heads">Bin/sqlite3/sqldiff.exe</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.Sqlite3/Windows/Bin/sqlite3/sqlite3.def?ref_type=heads">Bin/sqlite3/sqlite3.def</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.Sqlite3/Windows/Bin/sqlite3/sqlite3.dll?ref_type=heads">Bin/sqlite3/sqlite3.dll</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.Sqlite3/Windows/Bin/sqlite3/sqlite3.exe?ref_type=heads">Bin/sqlite3/sqlite3.exe</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.AndrewHazelden.Sqlite3/Windows/Bin/sqlite3/sqlite3_analyzer.exe?ref_type=heads">Bin/sqlite3/sqlite3_analyzer.exe</a></li>
