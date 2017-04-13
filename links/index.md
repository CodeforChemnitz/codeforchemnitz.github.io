---
layout: default
title: Links zu OpenData und OpenStreetmap
---

<div class="container">
	<div class="row">

		<div class="col-md-6">
			{% capture opendata %}{% include_relative _opendata.md %}{% endcapture %}
			{{ opendata | markdownify }}
		</div>
		<div class="col-md-6">
			{% capture osm_tools %}{% include_relative _osm_tools.md %}{% endcapture %}
			{{ osm_tools | markdownify }}
		</div>

	</div>
</div>
