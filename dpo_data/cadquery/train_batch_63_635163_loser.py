import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-36,0))
r=w0.sketch().segment((-42,-95),(-19,-100)).segment((-10,-59)).segment((39,-100)).segment((96,-31)).segment((67,-7)).segment((6,-61)).segment((6,-54)).segment((7,-51)).arc((-6,-44),(-4,-30)).segment((5,11)).segment((-18,16)).close().assemble().finalize().extrude(56).union(w0.workplane(offset=72/2).moveTo(-61.5,45).box(69,110,72))