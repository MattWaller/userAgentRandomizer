# userAgentRandomizer

<h1>Automatically Generate User agents</h1>

<strong>Installation</strong>
<p><code>
	pip install userAgentRandomizer
	</code></p>
<strong>To Use: </strong>


<p><code>
	from userAgentRandomizer import userAgents 
</code></p>
<p><code>
	ua = userAgents()
</code></p>
<p><code>
	random_useragent = ua.random()
</code></p>
<p><code>
	print(random_useragent)
</code></p>
<p><code>
	Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0
</code></p>
<p><code>
	print(ua.count())
</code></p>
<p><code>
	4513
</code></p>

<strong>Advanced Features: </strong>
<p>ua.random can pass one of the following options to 'engine', ["Chrome","Firefox","Edge","Opear","Safari"] - if no option selected it will return one at random.</p>

<p><code>
	print(ua.random('Firefox'))
</code></p>
<p><code>
	Mozilla/5.0 (Windows; U; Windows NT 6.1; hu; rv:1.9.1.9) Gecko/20100315 Firefox/3.5.9 (.NET CLR 3.5.30729)
</code></p>
