import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-51))
r=w0.workplane(offset=-29/2).moveTo(33,-30).cylinder(29,67).union(w0.sketch().push([(-93,29)]).circle(7).push([(17,44)]).circle(53).finalize().extrude(25)).union(w0.sketch().push([(-35,32)]).circle(50).push([(-35.5,31.5)]).rect(75,15,mode='s').finalize().extrude(131))