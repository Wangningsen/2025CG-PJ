import cadquery as cq
w0=cq.Workplane('YZ',origin=(-31,0,0))
w1=cq.Workplane('XY',origin=(0,0,-35))
r=w0.workplane(offset=-69/2).moveTo(27,-30).box(70,14,69).union(w0.sketch().push([(59,21)]).circle(24).push([(81,17)]).circle(1,mode='s').finalize().extrude(33)).union(w0.sketch().push([(-51.5,-35.5)]).rect(25,19).push([(-41,-37)]).circle(2,mode='s').finalize().extrude(51)).union(w1.workplane(offset=13/2).moveTo(65.5,-48.5).box(69,69,13))