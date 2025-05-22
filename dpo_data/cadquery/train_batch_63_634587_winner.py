import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,25,0))
r=w0.sketch().push([(-73,1.5)]).rect(54,19).push([(-20.5,-55.5)]).rect(39,19).push([(-20,-55)]).circle(9,mode='s').reset().face(w0.sketch().arc((44,-12),(99,13),(52,63)).arc((2,29),(44,-12)).assemble()).push([(39,25)]).circle(22,mode='s').finalize().extrude(-50).union(w0.workplane(offset=-9/2).moveTo(15,-10).cylinder(9,37))