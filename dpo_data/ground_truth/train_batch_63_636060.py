import cadquery as cq
w0=cq.Workplane('YZ',origin=(-54,0,0))
r=w0.sketch().push([(-49,27)]).circle(51).push([(-52,-11)]).circle(11,mode='s').push([(-49,26.5)]).rect(10,11,mode='s').push([(51,61.5)]).rect(98,39).push([(86,67)]).circle(6,mode='s').finalize().extrude(24).union(w0.workplane(offset=109/2).moveTo(3.5,-47).box(27,68,109))