import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,72))
r=w0.sketch().arc((-64,-100),(-41,-89),(-21,-74)).segment((64,-74)).segment((64,98)).segment((-58,98)).arc((-62,100),(-64,100)).segment((-64,70)).arc((-19,1),(-64,-70)).close().assemble().finalize().extrude(-144)