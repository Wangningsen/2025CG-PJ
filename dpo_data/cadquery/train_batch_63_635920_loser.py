import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-41))
r=w0.sketch().arc((-10,-1),(-2,-1),(-3,-9)).arc((11,10),(-10,-1)).assemble().finalize().extrude(-59).union(w0.sketch().segment((-42,-60),(-33,-60)).segment((-33,-66)).arc((25,-71),(72,-30)).arc((56,6),(64,43)).arc((-47,56),(-42,-60)).assemble().finalize().extrude(141))