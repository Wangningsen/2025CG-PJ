import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-52))
w1=cq.Workplane('YZ',origin=(-32,0,0))
r=w0.sketch().push([(-34,-27.5)]).rect(114,121).push([(58.5,-85.5)]).rect(65,29).finalize().extrude(-26).union(w1.workplane(offset=26/2).moveTo(75,53).cylinder(26,25))