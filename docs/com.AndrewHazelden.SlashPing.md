# Ping Slash Command
___

## Author
Andrew Hazelden

## Version
1.0

## Category
Console

___

## Description
<p>Ping is a console slash command that runs a network ping check. This can be used if you are having networking issues with your Fusion render nodes.</p>

<h2>Usage</h2>

<p>Step 1. Switch to the Fusion Console tab.<br>

Step 2. To run a network ping command type in:</p>

<pre>/ping &lt;hostname&gt;</pre>

<pre>/ping google.com</pre>

<p>If you wanted to ping your own system you can simply type in "/ping" with no address specified. Alternatively you could use:</p>

<pre>/ping localhost</pre>

<p>If you are on Mac/Linux you can ping your whole subnet using the "255.255.255.255" broadcast address:</p>

<pre>/ping 255.255.255.255</pre>

<h2>Output Example</h2>

<p>Check the ping time to Google via the internet:</p>

<pre>&gt; /ping google.com
PING google.com (173.237.125.21): 56 data bytes
64 bytes from 173.237.125.21: icmp_seq=0 ttl=58 time=18.836 ms
64 bytes from 173.237.125.21: icmp_seq=1 ttl=58 time=18.592 ms
64 bytes from 173.237.125.21: icmp_seq=2 ttl=58 time=17.990 ms

--- google.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 17.990/18.473/18.836/0.356 ms</pre>

___

## Dependencies

> [com.wesuckless.SlashCommand](com.wesuckless.SlashCommand.md)  
## Deploy

### Common (No Architecture)

> Scripts/SlashCommand/ping.lua  
