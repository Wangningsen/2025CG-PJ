import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-48,0))
r=w0.sketch().segment((-64,60),(-37,60)).segment((-37,-100)).segment((64,19)).segment((-30,100)).close().assemble().finalize().extrude(96)