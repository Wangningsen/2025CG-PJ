import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,48,0))
r=w0.sketch().arc((79,12),(100,56),(79,100)).close().assemble().finalize().extrude(-97).union(w0.sketch().arc((-100,-99),(-98,-99),(-98,-100)).arc((-97,-98),(-100,-99)).assemble().finalize().extrude(-49))