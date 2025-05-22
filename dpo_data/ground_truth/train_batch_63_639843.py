import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
r=w0.workplane(offset=-60/2).moveTo(28,0).cylinder(60,72).union(w0.sketch().segment((-100,-23),(-42,-40)).segment((-42,-36)).segment((7,-55)).segment((42,-66)).segment((69,23)).segment((-73,66)).close().assemble().finalize().extrude(31))