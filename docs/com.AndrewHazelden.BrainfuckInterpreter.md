# Brainfuck Interpreter
___

## Author
Andrew Hazelden

## Version
1.0

## Category
Fun/Console

___

## Description
<p>An interpreter to run the "Brainfuck" language in the console. For Brainfuck usage tips switch to the Console tab and type in "bfq help".</p>
	
<p>The language consists of only eight simple commands and an instruction pointer.</p>

<p>While it is fully Turing-complete, it is not intended for practical use, but to challenge and amuse programmers.</p>

<h3>Wikpedia Brainfuck Topic:</h3>
<p>https://en.wikipedia.org/wiki/Brainfuck</p>

<p>There are eight commands:</p>

<pre>
	&lt; - Decrease the pointer
	&gt; - Increase the pointer
	+ - Increase the current cell value
	- - Decrease the current cell value
	[ - Declare a loop
	] - Declare the end of a loop
	. - Display the current cell value in ASCII
	, - Read the user's input into the cell
</pre>

<p>A loop gets executed when the current cell has a value greater than zero. Cells overflow and underflow. The pointer does so too.</p>

<p>For Brainfuck usage details type the following text in the Console:</p>

<pre>bfq help</pre>

<p>Brainfuck Example 1 (Hello World):</p>

<pre>bfq ++++++++++[&gt;+++++++&gt;++++++++++&gt;+++&gt;+&lt;&lt;&lt;&lt;-]&gt;++.&gt;+.+++++++..+++.&gt;++.&lt;&lt;+++++++++++++++.&gt;.+++.------.--------.&gt;+.&gt;.</pre>


___

## Dependencies

## Deploy

### Common (No Architecture)

> Fuses/Console/Brainfuck Interpreter.fuse  
