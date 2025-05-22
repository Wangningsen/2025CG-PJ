import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,12,0))
r=w0.sketch().push([(92,79)]).circle(8).push([(92,77.5)]).rect(2,7,mode='s').push([(97.5,79)]).rect(3,4,mode='s').finalize().extrude(-27).union(w0.workplane(offset=3/2).moveTo(-59,-60.5).box(82,53,3))