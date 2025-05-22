import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.sketch().segment((17,55),(24,32)).segment((57,41)).segment((51,65)).segment((37,61)).arc((33,46),(23,57)).close().assemble().finalize().extrude(-63).union(w0.workplane(offset=137/2).moveTo(-39,-47).cylinder(137,18))