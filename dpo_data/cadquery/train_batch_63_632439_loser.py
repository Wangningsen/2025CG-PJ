import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-29))
w1=cq.Workplane('ZX',origin=(0,-35,0))
r=w0.sketch().segment((-47,-8),(-44,-8)).segment((-44,-17)).segment((-7,-17)).segment((-7,-59)).segment((47,-59)).segment((47,17)).segment((26,17)).segment((26,39)).segment((13,39)).arc((-11,59),(-35,39)).segment((-47,39)).close().assemble().reset().face(w0.sketch().segment((7,-17),(15,-34)).segment((33,-28)).segment((26,-10)).segment((26,-17)).close().assemble(),mode='s').finalize().extrude(129).union(w1.workplane(offset=27/2).moveTo(-63.5,20).box(73,40,27))