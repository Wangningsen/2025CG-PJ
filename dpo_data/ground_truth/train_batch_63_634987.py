import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,48))
r=w0.sketch().segment((-100,-65),(23,-65)).segment((23,-15)).arc((100,24),(17,45)).segment((-100,45)).close().assemble().finalize().extrude(-96).union(w0.sketch().segment((2,-9),(50,-32)).segment((73,16)).arc((45,20),(25,39)).close().assemble().finalize().extrude(-11))