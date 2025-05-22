import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-42,0))
w1=cq.Workplane('XY',origin=(0,0,52))
r=w0.sketch().segment((-100,-82),(-76,-82)).segment((-76,-90)).segment((-29,-90)).segment((-29,-82)).segment((-4,-82)).segment((-4,2)).segment((-29,2)).segment((-29,10)).segment((-76,10)).segment((-76,2)).segment((-100,2)).close().assemble().push([(-52.5,-39.5)]).rect(93,55,mode='s').finalize().extrude(27).union(w1.sketch().arc((55,-41),(90,0),(55,42)).close().assemble().finalize().extrude(48))