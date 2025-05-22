import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-1,0))
w1=cq.Workplane('YZ',origin=(-19,0,0))
r=w0.sketch().segment((7,-35),(60,-55)).segment((62,-49)).segment((10,-29)).close().assemble().finalize().extrude(-14).union(w0.workplane(offset=43/2).moveTo(-58.5,12.5).box(83,69,43)).union(w1.sketch().segment((-42,18),(-29,18)).segment((-29,-7)).segment((25,-7)).segment((25,18)).segment((39,18)).segment((39,74)).segment((25,74)).segment((25,100)).segment((-29,100)).segment((-29,74)).segment((-42,74)).close().assemble().finalize().extrude(74))