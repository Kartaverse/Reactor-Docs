# JSON Reader
___

## Author
Blazej Floch

## Version
1.0

## Category
Modifiers

___

## Description
<p>A modifier that picks a value from a JSON File.</p>

<h2>Usage</h2>

<p>Given a JSON dataset like:</p>
<pre>{
   "dataset": {
        "metadata": &#91;"Hello", "World"&#93;
   }
}</pre>
<p>... loaded from a file, and a Key set to:</p>
<pre>dataset.metadata.2</pre>
<p>... results in the value "World". Note that arrays indices begin with 1, like with Lua, not 0.</p>

<h2>Array access via Frames</h2>

<p>You can access arrays based on frame number by making the Key input a SimpleExpression like:</p>
</pre>Text("dataset.metadata." .. time)</pre>

<h2>Notes</h2>

<p>In order to access keys with . the separator can be changed.</p>
<p>If the JSON file can not be loaded, or the field is not found a default value can be supplied. It will be returned as fallback by the modifier.</p>




___

## Dependencies

## Deploy

### Common (No Architecture)

<ul>
<li><a href="https://gitlab.com/WeSuckLess/Reactor/-/blob/master/Atoms/com.bfloch.JSONReader/Fuses/Modifiers/JSONReader.fuse?ref_type=heads">Fuses/Modifiers/JSONReader.fuse</a></li>
</ul>
