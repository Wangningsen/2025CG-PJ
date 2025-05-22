import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,84,0))
w1=cq.Workplane('ZX',origin=(0,27,0))
r=w0.sketch().push([(18.5,70)]).rect(85,60).push([(38,-55)]).circle(45).circle(18,mode='s').finalize().extrude(-110).union(w0.sketch().arc((13,-66),(62,-69),(36,-27)).arc((-75,13),(13,-66)).assemble().finalize().extrude(-78)).union(w1.workplane(offset=-112/2).moveTo(38,-55).box(50,72,112))