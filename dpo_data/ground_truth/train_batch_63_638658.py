import cadquery as cq
w0=cq.Workplane('YZ',origin=(5,0,0))
w1=cq.Workplane('ZX',origin=(0,-50,0))
r=w0.sketch().push([(3,-54)]).circle(46).push([(29,79)]).circle(21).finalize().extrude(-87).union(w0.workplane(offset=76/2).moveTo(-31,39).cylinder(76,14)).union(w1.sketch().arc((61,16),(63,26),(61,35)).close().assemble().finalize().extrude(75))