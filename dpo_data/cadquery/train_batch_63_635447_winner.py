import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,13,0))
r=w0.sketch().segment((-98,-23),(-70,-39)).segment((-14,-100)).segment((10,-77)).segment((46,-91)).segment((70,-42)).arc((30,3),(56,54)).segment((18,100)).segment((-7,77)).segment((-45,91)).close().assemble().push([(81,9)]).circle(17).finalize().extrude(-26)