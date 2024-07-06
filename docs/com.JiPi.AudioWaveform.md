# AudioWaveform
___

## Author
JiPi

## Version
1.9

## Category
Tools/Miscellaneous

___

## Description
<center><h2>AudioWaveform</h2></center>
<p>The tool (Fuse) visualizes a 16bit PCM WAV file. The WAV file must not exceed now (V1.9) 200 MB. The data can be zoomed and moved.</p>
<p>The play point is set in the middle of the picture. Based on the fuse modifier SuckLessAudioModifier by Pieter Van Houte.

<p>-                      </p>

<font color="yellow"> Waveformparameter:</font>
<p>There are three parameters for setting the waveform's timing: 1) Proxy 2) Zoom 3) Resolution</p>
 
<ol>
	<li>Proxy: This multiplies the sample pool without increasing the number of pixels shown</li>
	<li>Zoom: This also multiplies the sample pool, but all values ​​are also displayed (as far as can be displayed)</li>
	<li>Resolution: Acts as a divisor for the displayable pixels -> Resolution = 2 with HD -> 1920/2</li>
	<li></li>
</ol>

<p>You can choose left, right and stereo channel. The stereo signal (Both) is generated by maximum formation of the two channels.</p>
<p>After loading the data from file, arrays will be filled with nummerical data. The size of the audio file is limited to 50 MB in order not to make the arrays too large.</p>
<p>The audio data can be moved forward or backward by up to 50 frames. A crosshair can be shown and two different envelopes can be selected.</p>

<p>-                      </p>

<font color="yellow"> Amplitude Spectrum:</font>
<p>An amplitude spectrum of the loaded WAV file can be displayed instead of the waveform (control page spectrum) 
Attention: The correct settings for the waveform should then be set to 1 for proxy, zoom and resolution. Only then will the FFT display the mathematically correct spectrum. 
However, interesting effects can also be achieved with this parameters. <p>
<p>The FFT window is configurable. There are 4 different types of display: raw, bars, smooth and needles. 
The support points can be set equidistant. Then sections can be combined, which are also shown in the 4 forms. 
The color of the spectrum can be set via the color control page.<p>

<p>If you have selected the display of the spectrum, the "Elongation" functionality can be activated. 
A window above the spectrum can be selected here with offset and width. The selected data are calculated with the "Operator" parameter to be set and visualized as a bar. 
This value "Elongation" can be used by other nodes by "Connect to".<p>

<p>-                      </p>

<font color="yellow"> Steady Waveform:</font>
<p>With the "Steady Waveform" functionality, you can determine how much audio data a so-called seed frame is formed from by selecting the number of frames. 
The seed frames are output directly, the "missing" are calculated.<p>

<p>-                      </p>

<font color="yellow"> Filter:</font>
<p>The Samplingdata can be filtered by three frequency bands: Lowpass 0-300 Hz, Bandpass 300 Hz - 3kHz and Highpass 3kHz-20kHz.<p>

<p>-                      </p>

<font color="yellow"> Elongation with Schmitt-Trigger:</font>
<p>Elongation can be mapped to On/Off-Values with Hystersis.<p>

<p>Elongation for Spectrum has now three Elongations. Each can set to separate Frequencyband with Bandwidth, Offset and Amplify<p>


<p><font color="fuchsia"> If you like this fuse, I would be happy to receive a message ( <a href="https://www.steakunderwater.com/wesuckless/memberlist.php?mode=viewprofile&u=4700">JiiPii</a> ). 
</font><p>

<p>See also my post in WSL "/Fusion Studio/Scripting, Fuses and Macros:    </p>
<a href="https://www.steakunderwater.com/wesuckless/viewtopic.php?f=6&t=4191&p=32728#p32728">&#91;Fuse&#93; AudioWaveform</a>
<p>And a short Youtube Tutorial: </p>
<a href="https://youtu.be/KY3L-qM9EQA">AudioWaveform in Davinci Resolve Fusion</a>

<p><font color="yellow">Versions:</p>
<table border="0" cellpadding="5">
	<tr><td>0.1</td><td>First Try</td></tr>
	<tr><td>0.2</td><td>Reactor Version</td></tr>
	<tr><td>0.3</td><td> FFT beta,	Implematation of a FFT to show an Equalizer - Test how much Resources and Computingtime is needed</td></tr>
	<tr><td>0.4</td><td> Amplitude Spectrum - Implementation of Amplitude Spectrum. Choose a frequency band, generate a "modifier" Value for "connect to" functionality</td></tr>
	<tr><td>0.5</td><td> Beauty Work - Bugfixes: Display Audiodata, SampleRead Stereo, Spectrum vs Waveformenvelope control,	Spectrum Appearance: Rough,Bars,Smooth,Needles</td></tr>
	<tr><td>0.6</td><td> FFT window width selectable (256 - 2048), Scale FFT, Equidistance support points with selectable Steps,	FFT Limitation with Compression</td></tr>
	<tr><td>0.7</td><td> Bugfix: No "Connect to" Data (Elongation), if Fuse not networked, Show Errors in Image: 1) File too large 2) Unsupported WAV-File format</td></tr>
	<tr><td>0.8</td><td> Optimization of sampleread ( 30% faster ), Elongation for Waveform,	Steady Waveform, Filter implemented (LP,BP,HP),	New Controltab:  On/Off Elongation with Hysterese, Change Spectrumvalue to logarithmic,	Limitation and Logarithmic is considered for Elongation</td></tr>
	<tr><td>0.9</td><td> Hide Selection Tool (Elongation), Smooth Filled for Spectrumsvisualation, BugFix: MapPath</td></tr>
	<tr><td>1.0</td><td> Additional Error: Wrong bit-depth, 	Filter/File/Elongationinputs to INP_External = false - avoidance of weird behavior</td></tr>
	<tr><td>1.1</td><td> Implement of three Elongationsets for Spectrum, added Offset, Bugfix equidistant points</td></tr>
	<tr><td>1.2</td><td> Add Noisethreshold for Waveform</td></tr>
	<tr><td>1.3</td><td> Frequency Visualization (Shadertoy) - Interface Audiodata, Smoothfunctionality for Frequency Visualization, Possibility of multiple use of the FrequencyVisualization in one Composition, Add Decompressfunctionality in Spectrum(equidistant/logarithmic) with Treshhold</td></tr>
	<tr><td>1.4</td><td> DCTL corrected,	Added a merge for Backgroundpicture for Frequency Visualization</td></tr>
	<tr><td>1.5</td><td> Workaround Fusion17 for Waveformdisplay(MoveTo shows line return for normal and positiv envelope), Added "Smooth"-Feature for Spectrumdisplay. Falling edges are output with a delay</td></tr>
	<tr><td>1.6</td><td> Added Slope-Feature - you can choose a corner frequency from which a continuous amplification is carried out, so that high frequencies are raised, Added a JiPi-Logo</td></tr>
	<tr><td>1.7</td><td> Bugfix</td></tr>
	<tr><td>1.8</td><td> Shadertoy Audio (more Information: <a href="https://nmbr73.github.io/Shaderfuse/Audio/">ShaderfuseAudio</a>) </td></tr>
	<tr><td>1.9</td><td> Bugfix "Input Texture", Small Changes, Logo, 200MB Limit</td></tr>
</table>


<p><font color="fuchsia">Known Bugs:</p>
<p><font color="white">If you use the elongation within an expression of another fuse, this is only operated if the AudioWaveform is connected to the active network.
Contrary to the Connect_To functionality. Workaround would be to add an input in the target fuse (edit controls) and fill it with Connect_to,
then an expression can be entered at the target input.</p>


___

## Dependencies

## Deploy

### Common (No Architecture)

> Fuses/Miscellaneous/AudioWaveform.fuse  