import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,3,0))
r=w0.sketch().arc((-55,-49),(-57,-92),(-14,-89)).close().assemble().push([(20,54)]).circle(46).finalize().extrude(-76).union(w0.workplane(offset=-40/2).moveTo(-47,-6.5).box(34,5,40)).union(w0.workplane(offset=70/2).moveTo(-47,-7).cylinder(70,14))