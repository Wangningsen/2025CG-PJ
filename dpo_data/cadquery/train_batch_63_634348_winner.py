import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-45,0))
r=w0.sketch().segment((-82,-66),(-68,-66)).arc((-35,-95),(7,-98)).segment((33,-18)).segment((68,-29)).segment((68,10)).segment((54,10)).arc((-6,44),(-68,10)).segment((-82,10)).close().assemble().push([(50,68)]).circle(32).finalize().extrude(90)