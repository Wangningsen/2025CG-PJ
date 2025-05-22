import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
w1=cq.Workplane('XY',origin=(0,0,6))
r=w0.sketch().segment((-68,21),(-66,21)).segment((-66,-28)).segment((-6,-80)).segment((68,6)).segment((-18,80)).close().assemble().push([(-12,0)]).circle(27,mode='s').finalize().extrude(-98).union(w0.workplane(offset=102/2).moveTo(-11.5,0).box(105,60,102)).union(w1.workplane(offset=8/2).moveTo(0,15).cylinder(8,25))