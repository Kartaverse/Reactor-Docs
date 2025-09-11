# PROPAGATE - change parameters across multiple nodes
___

## Category
Scripts

## Author
Dominik Bargiel

## Version
1.0

___

## Description
<h1>PROPAGATE – change parameters across multiple nodes</h1> <p>PROPAGATE is a utility that captures parameter changes on the active node and applies them to other selected nodes, keeping settings, connections, expressions, and animations consistent across a selection. It streamlines multi-node work by supporting all parameter types with special handling for Loader/Saver tools, point inputs, and keyframed animation.</p>
<a href="https://youtu.be/yT1KqW1dVRw">Watch the PROPAGATE tutorial on YouTube</a>

<h2>Key Features:</h2> <ul> <li><strong>Simple Interface</strong> – Minimal, window-based UI for quick capture and apply actions.</li> <li><strong>Change Capture & Apply</strong> – Records edits on demand and propagates them when commanded.</li> <li><strong>Universal Parameter Support</strong> – Handles all parameter types, including FuID and enumeration values.</li> <li><strong>Robust Table Handling</strong> – Compares and updates table-based parameters safely and accurately.</li> <li><strong>Loader/Saver & Point Aware</strong> – Special logic for media tools and point parameters.</li> <li><strong>Connection Propagation</strong> – Mirrors input connections and disconnections across nodes.</li> <li><strong>Output Routing Propagation</strong> – Replicates output connections to the same downstream targets.</li> <li><strong>Expression Propagation</strong> – Copies expressions alongside values wherever used.</li> <li><strong>Keyframe/Animation Support</strong> – Transfers keyframes and animated curves reliably.</li> <li><strong>Full Input Iteration</strong> – Scans all tool inputs for comprehensive change detection.</li> </ul> <h2>How to Use:</h2> <ol> <li><strong>Select Nodes:</strong> Choose 2 or more nodes to synchronize.</li> <li><strong>Open PROPAGATE:</strong> Press <strong>I</strong> to launch the PROPAGATE window.</li> <li><strong>Edit the Active Node:</strong> Make parameter changes, connect or disconnect inputs/outputs, or add/modify expressions.</li> <li><strong>Apply Changes:</strong> Click <strong>Apply Changes</strong> to propagate updates to all selected nodes.</li> <li><strong>Cancel:</strong> Press <strong>ESC</strong> to close without applying.</li> </ol>

___

## Donation
The author of the atom has suggested a donation of "1".  
You can donate using the URL: <a href="http://www.paypal.me/dominikbargiel">http://www.paypal.me/dominikbargiel</a>

## Download

Download a zipped atom package for offline installation:
> [com.DominikBargiel.Propagate.zip](https://gitlab.com/WeSuckLess/Reactor/-/archive/master/Reactor-master.zip?path=Atoms/com.DominikBargiel.Propagate)  

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Propagate/Config/Propagate/Propagate.fu?ref_type=heads">Config/Propagate/Propagate.fu</a></li>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.DominikBargiel.Propagate/Config/Propagate/Propagate.lua?ref_type=heads">Config/Propagate/Propagate.lua</a></li>
</ul>
