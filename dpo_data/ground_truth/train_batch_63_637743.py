import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,47,0))
r=w0.sketch().push([(-49,-70.5)]).rect(52,59).push([(-49,-70)]).circle(9,mode='s').finalize().extrude(-102).union(w0.workplane(offset=-41/2).moveTo(30,-21).box(44,52,41)).union(w0.sketch().arc((29,21),(18,-61),(55,13)).segment((75,93)).segment((50,100)).close().assemble().finalize().extrude(8))