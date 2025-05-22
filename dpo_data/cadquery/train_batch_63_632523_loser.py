import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,57,0))
w1=cq.Workplane('YZ',origin=(-17,0,0))
r=w0.sketch().segment((80,16),(100,8)).arc((93,14),(83,17)).close().assemble().finalize().extrude(-69).union(w1.sketch().segment((-55,-100),(62,-100)).segment((62,-21)).segment((29,-21)).arc((25,-11),(20,-1)).segment((20,23)).segment((-55,23)).segment((-55,-1)).arc((-62,-24),(-55,-47)).close().assemble().finalize().extrude(14))