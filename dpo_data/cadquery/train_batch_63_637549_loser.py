import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,39))
r=w0.sketch().segment((15,-21),(31,-48)).segment((100,-6)).segment((84,20)).close().assemble().finalize().extrude(-78).union(w0.sketch().push([(-90,-45)]).circle(10).reset().face(w0.sketch().arc((-63,18),(2,-10),(-31,52)).segment((-63,52)).close().assemble()).push([(-21.5,10)]).rect(5,14,mode='s').finalize().extrude(-10))