import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-35,0))
w1=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().push([(17,-48)]).circle(41).circle(26,mode='s').finalize().extrude(9).union(w0.workplane(offset=30/2).moveTo(-93,-73).cylinder(30,7)).union(w1.sketch().arc((42,75),(89,33),(46,81)).arc((48,76),(42,75)).assemble().finalize().extrude(25))