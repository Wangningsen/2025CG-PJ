import cadquery as cq
w0=cq.Workplane('YZ',origin=(6,0,0))
w1=cq.Workplane('ZX',origin=(0,-50,0))
r=w0.sketch().push([(3,-54)]).circle(46).push([(29,79)]).circle(21).finalize().extrude(-87).union(w0.workplane(offset=75/2).moveTo(-31,39).cylinder(75,14)).union(w1.sketch().arc((61,6),(63,21),(61,35)).close().assemble().finalize().extrude(75))