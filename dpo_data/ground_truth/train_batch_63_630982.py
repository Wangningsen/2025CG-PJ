import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-1,0))
w1=cq.Workplane('YZ',origin=(55,0,0))
r=w0.sketch().segment((5,-35),(60,-55)).segment((63,-49)).arc((29,-3),(62,41)).segment((36,51)).close().assemble().finalize().extrude(-13).union(w0.workplane(offset=44/2).moveTo(-58.5,12.5).box(83,69,44)).union(w1.sketch().segment((-42,18),(-28,18)).segment((-28,-7)).segment((25,-7)).segment((25,18)).segment((40,18)).segment((40,74)).segment((25,74)).segment((25,100)).segment((-28,100)).segment((-28,74)).segment((-42,74)).close().assemble().finalize().extrude(-74))