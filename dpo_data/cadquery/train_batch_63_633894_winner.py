import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
w1=cq.Workplane('XY',origin=(0,0,-7))
r=w0.workplane(offset=-200/2).moveTo(-7.5,-38).box(33,26,200).union(w1.sketch().push([(16,69)]).rect(70,44).push([(-20,63)]).circle(3,mode='s').push([(27,80)]).circle(4,mode='s').finalize().extrude(31))