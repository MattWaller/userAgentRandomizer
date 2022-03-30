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