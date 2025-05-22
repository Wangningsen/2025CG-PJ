import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,68,0))
w1=cq.Workplane('ZX',origin=(0,66,0))
r=w0.sketch().push([(-18,-12.5)]).rect(78,121).push([(14,-20)]).circle(7,mode='s').finalize().extrude(-135).union(w1.sketch().arc((-86,25),(-92,-34),(-55,-81)).segment((-55,-85)).segment((-46,-85)).arc((-18,-91),(11,-85)).segment((100,-85)).segment((100,42)).segment((38,42)).arc((8,61),(-28,65)).arc((-83,85),(-86,25)).assemble().finalize().extrude(-22))