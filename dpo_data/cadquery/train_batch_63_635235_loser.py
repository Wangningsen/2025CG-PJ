import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,39))
r=w0.sketch().segment((-44,75),(-39,17)).arc((-70,-76),(-30,13)).segment((15,15)).segment((8,80)).close().assemble().finalize().extrude(-84).union(w0.sketch().arc((99,-71),(100,-57),(99,-43)).close().assemble().finalize().extrude(5))