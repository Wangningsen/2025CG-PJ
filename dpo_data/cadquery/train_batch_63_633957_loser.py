import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
w1=cq.Workplane('ZX',origin=(0,3,0))
r=w0.workplane(offset=-108/2).moveTo(17,52).cylinder(108,38).union(w0.sketch().segment((30,-81),(37,-90)).segment((85,-55)).segment((72,-49)).close().assemble().finalize().extrude(92)).union(w1.sketch().segment((-85,42),(-40,42)).arc((-63,47),(-85,42)).assemble().finalize().extrude(-48))