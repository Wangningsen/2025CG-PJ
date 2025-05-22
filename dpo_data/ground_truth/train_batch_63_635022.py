import cadquery as cq
w0=cq.Workplane('YZ',origin=(-31,0,0))
w1=cq.Workplane('XY',origin=(0,0,-35))
r=w0.workplane(offset=-69/2).moveTo(27,-30.5).box(70,13,69).union(w0.sketch().segment((82,19),(83,19)).segment((83,22)).segment((82,22)).arc((35,23),(82,19)).assemble().finalize().extrude(33)).union(w0.sketch().push([(-51.5,-36)]).rect(25,18).push([(-41,-39)]).circle(2,mode='s').finalize().extrude(51)).union(w1.workplane(offset=13/2).moveTo(65.5,-48.5).box(69,69,13))