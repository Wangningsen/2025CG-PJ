import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,29,0))
w1=cq.Workplane('XY',origin=(0,0,-31))
r=w0.workplane(offset=51/2).moveTo(-8,-56).cylinder(51,44).union(w1.sketch().segment((-82,6),(36,6)).segment((36,-80)).segment((98,-80)).segment((98,6)).segment((100,6)).segment((100,75)).segment((-82,75)).close().assemble().finalize().extrude(83))