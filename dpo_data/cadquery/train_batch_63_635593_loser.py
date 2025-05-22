import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,49,0))
r=w0.sketch().arc((79,12),(100,56),(79,100)).close().assemble().finalize().extrude(-98).union(w0.sketch().segment((-100,-99),(-97,-100)).arc((-99,-99),(-100,-99)).assemble().finalize().extrude(-51))