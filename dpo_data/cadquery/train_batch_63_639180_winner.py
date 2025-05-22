import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,57,0))
r=w0.sketch().segment((-42,-67),(-28,-100)).segment((18,-80)).segment((17,-78)).arc((12,99),(-42,-67)).assemble().finalize().extrude(-128).union(w0.sketch().segment((-59,2),(-43,-33)).segment((59,16)).segment((43,51)).close().assemble().finalize().extrude(14))