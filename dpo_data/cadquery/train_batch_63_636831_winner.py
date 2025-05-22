import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
r=w0.sketch().segment((-68,21),(-66,20)).segment((-66,-28)).segment((-5,-80)).segment((68,6)).segment((-19,80)).segment((-66,23)).close().assemble().push([(-12,0)]).circle(27,mode='s').finalize().extrude(-98).union(w0.workplane(offset=102/2).moveTo(-11.5,0).box(105,60,102))