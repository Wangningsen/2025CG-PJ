import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,32))
r=w0.sketch().segment((-93,25),(-91,-7)).segment((-62,-5)).segment((-64,27)).close().assemble().finalize().extrude(-65).union(w0.sketch().arc((47,88),(-88,-47),(100,-10)).arc((57,36),(47,88)).assemble().finalize().extrude(-39))