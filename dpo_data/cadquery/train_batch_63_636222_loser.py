import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-72))
r=w0.sketch().arc((-64,-100),(-45,-91),(-25,-78)).segment((-25,-74)).segment((64,-74)).segment((64,98)).segment((-64,100)).segment((-64,72)).arc((-19,0),(-64,-72)).close().assemble().finalize().extrude(144)