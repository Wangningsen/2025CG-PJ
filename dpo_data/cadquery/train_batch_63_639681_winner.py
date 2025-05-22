import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,15,0))
w1=cq.Workplane('YZ',origin=(-8,0,0))
r=w0.sketch().segment((-77,-49),(-66,-49)).segment((-67,35)).segment((-77,35)).close().assemble().push([(-72,-7)]).circle(4,mode='s').finalize().extrude(85).union(w1.workplane(offset=57/2).moveTo(-47,24).cylinder(57,53))