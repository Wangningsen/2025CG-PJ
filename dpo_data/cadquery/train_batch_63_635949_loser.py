import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-18,0))
r=w0.workplane(offset=-6/2).moveTo(17,90).cylinder(6,10).union(w0.sketch().segment((-63,-84),(-13,-100)).segment((4,-44)).arc((72,-47),(36,12)).arc((15,14),(8,-7)).arc((4,-16),(3,-26)).segment((-42,-19)).segment((-46,-39)).arc((-77,-41),(-55,-62)).close().assemble().finalize().extrude(42))