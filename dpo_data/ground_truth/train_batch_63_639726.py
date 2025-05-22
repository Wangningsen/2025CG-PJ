import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-33))
w1=cq.Workplane('XY',origin=(0,0,-87))
r=w0.sketch().segment((-36,-37),(-33,-37)).segment((-33,-83)).segment((91,-83)).segment((91,-37)).segment((94,-37)).segment((94,-21)).segment((91,-21)).segment((91,24)).segment((-33,24)).segment((-33,-21)).segment((-36,-21)).close().assemble().finalize().extrude(2).union(w0.sketch().push([(29,-29.5)]).rect(142,121).rect(112,85,mode='s').finalize().extrude(120)).union(w1.workplane(offset=121/2).moveTo(-61,51).cylinder(121,39))