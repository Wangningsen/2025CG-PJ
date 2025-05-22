import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-18,0))
r=w0.workplane(offset=-6/2).moveTo(17,91).cylinder(6,9).union(w0.sketch().segment((-63,-84),(-13,-100)).segment((5,-40)).arc((74,-43),(34,12)).arc((14,13),(8,-6)).arc((3,-19),(3,-33)).segment((-42,-19)).segment((-49,-39)).arc((-78,-42),(-56,-62)).close().assemble().finalize().extrude(42))