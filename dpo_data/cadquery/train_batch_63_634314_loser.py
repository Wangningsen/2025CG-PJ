import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-46,0))
r=w0.sketch().push([(-68.5,33.5)]).rect(63,93).push([(-68,34)]).circle(17,mode='s').push([(66,-46)]).circle(34).push([(97,-41)]).circle(2,mode='s').finalize().extrude(92)