import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,23))
w1=cq.Workplane('YZ',origin=(-21,0,0))
r=w0.sketch().push([(-69,82)]).circle(18).push([(-62,88)]).circle(5,mode='s').finalize().extrude(-101).union(w0.sketch().push([(52,-83)]).rect(70,34).push([(52.5,-83)]).rect(3,12,mode='s').push([(74,-71)]).rect(10,8,mode='s').finalize().extrude(55)).union(w1.workplane(offset=-13/2).moveTo(73,29).cylinder(13,23))