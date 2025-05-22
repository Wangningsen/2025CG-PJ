import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,7))
w1=cq.Workplane('YZ',origin=(19,0,0))
r=w0.sketch().segment((-96,-47),(-89,-53)).segment((-66,-22)).segment((-73,-17)).segment((-76,-20)).arc((-75,-23),(-78,-24)).close().assemble().finalize().extrude(-107).union(w0.workplane(offset=93/2).moveTo(45,25).cylinder(93,21)).union(w1.workplane(offset=77/2).moveTo(25,4).cylinder(77,28))