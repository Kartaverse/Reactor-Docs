# Instant Meshes
___

## Author
 : Wenzel Jakob, Marco Tarini, Daniele Panozzo, Olga Sorkine-Hornung

## Version
 : v1.0

## Category
 : Bin
___

## Description
<p><a href="https://github.com/wjakob/instant-meshes">Instant Meshes</a> is a cross-platform open-source automatic mesh retopology program. It's an Interactive field-aligned mesh generator that runs either from a GUI session or CLI (command-line).</p>

<h2>Open-Source License</h2>
<p>Modified BSD License (3-Clause BSD License)</p>
<p>The Instant Meshes atom was packaged by Andrew Hazelden.</p>


<h2>For More information</h2>
<p>Instant Meshes GitHub<br>
<a href="https://github.com/wjakob/instant-meshes">https://github.com/wjakob/instant-meshes</a></p>

<p>Instant Field Aligned Meshes (SIGGRAPH ASIA 2015) Video<br>
<a href="https://www.youtube.com/watch?v=U6wtw6W4x3I">https://www.youtube.com/watch?v=U6wtw6W4x3I</a></p>

<p>Instant Field-Aligned Meshes PDF<br>
<a href="https://igl.ethz.ch/projects/instant-meshes/i
nstant-meshes-SA-2015-jakob-et-al.pdf">https://igl.ethz.ch/projects/instant-meshes/instant-meshes-SA-2015-jakob-et-al.pdf</a></p>

<p>IGL - Instant Field-Aligned Meshes Homepage<br>
<a href="https://igl.ethz.ch/projects/instant-meshes/">https://igl.ethz.ch/projects/instant-meshes/</a></p>

<h2>Command Line Options</h2>

<pre>
Options:
   -o, --output <output>     Writes to the specified PLY/OBJ output file in batch mode
   -t, --threads <count>     Number of threads used for parallel computations
   -d, --deterministic       Prefer (slower) deterministic algorithms
   -c, --crease <degrees>    Dihedral angle threshold for creases
   -S, --smooth <iter>       Number of smoothing & ray tracing reprojection steps (default: 2)
   -D, --dominant            Generate a tri/quad dominant mesh instead of a pure tri/quad mesh
   -i, --intrinsic           Intrinsic mode (extrinsic is the default)
   -b, --boundaries          Align to boundaries (only applies when the mesh is not closed)
   -r, --rosy <number>       Specifies the orientation symmetry type (2, 4, or 6)
   -p, --posy <number>       Specifies the position symmetry type (4 or 6)
   -s, --scale <scale>       Desired world space length of edges in the output
   -f, --faces <count>       Desired face count of the output mesh
   -v, --vertices <count>    Desired vertex count of the output mesh
   -C, --compat              Compatibility mode to load snapshots from old software versions
   -k, --knn <count>         Point cloud mode: number of adjacent points to consider
   -F, --fullscreen          Open a full-screen window
   -h, --help                Display this message
</pre>
___

## Dependencies


___

## Deploy

### Common (No Architecture)

> Bin/instantmeshes/LICENSE.txt  
> Bin/instantmeshes/README.html  
> Bin/instantmeshes/README.md  

### macOS

> Bin/instantmeshes/InstantMeshes.app/Contents/Info.plist  
> Bin/instantmeshes/InstantMeshes.app/Contents/MacOS/Instant Meshes  
> Bin/instantmeshes/InstantMeshes.app/Contents/Resources/im.icns  
