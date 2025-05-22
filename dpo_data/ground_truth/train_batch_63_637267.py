import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-3,0))
r=w0.sketch().arc((-80,64),(-74,17),(-27,25)).arc((-18,92),(-80,64)).assemble().push([(-55,43)]).circle(4,mode='s').finalize().extrude(-44).union(w0.workplane(offset=22/2).moveTo(24,-55).cylinder(22,39)).union(w0.workplane(offset=49/2).moveTo(43,-55).cylinder(49,45))