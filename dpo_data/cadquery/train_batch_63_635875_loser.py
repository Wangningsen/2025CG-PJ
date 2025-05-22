import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
r=w0.sketch().segment((32,6),(52,3)).segment((64,69)).segment((44,72)).close().assemble().finalize().extrude(-89).union(w0.sketch().segment((-64,-72),(40,-72)).segment((40,-37)).arc((6,0),(40,29)).segment((40,49)).segment((-64,49)).close().assemble().push([(-52,-65)]).circle(2,mode='s').finalize().extrude(111))