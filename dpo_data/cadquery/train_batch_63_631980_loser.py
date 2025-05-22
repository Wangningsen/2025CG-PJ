import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-12,0))
r=w0.sketch().segment((-45,-61),(4,-61)).segment((4,-82)).segment((16,-66)).segment((-39,-30)).segment((-40,-31)).arc((-100,-33),(-45,-55)).close().assemble().push([(92,52.5)]).rect(16,59).finalize().extrude(24)