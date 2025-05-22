import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,45,0))
r=w0.sketch().segment((-82,-66),(-69,-66)).arc((-32,-96),(15,-95)).segment((33,-18)).segment((68,-29)).segment((68,10)).segment((51,10)).arc((-6,44),(-69,10)).segment((-82,10)).close().assemble().push([(50,68)]).circle(32).finalize().extrude(-89)