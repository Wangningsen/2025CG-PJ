import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-72))
r=w0.sketch().arc((-64,-100),(-44,-91),(-24,-77)).segment((-23,-74)).segment((64,-74)).segment((64,98)).segment((-61,98)).segment((-61,100)).segment((-64,100)).segment((-64,71)).arc((-19,0),(-64,-71)).close().assemble().finalize().extrude(144)