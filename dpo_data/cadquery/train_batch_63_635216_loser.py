import cadquery as cq
w0=cq.Workplane('YZ',origin=(27,0,0))
w1=cq.Workplane('YZ',origin=(36,0,0))
r=w0.sketch().segment((-41,-100),(31,-100)).segment((31,-17)).segment((-22,-17)).arc((-25,-1),(-28,-17)).segment((-41,-17)).close().assemble().finalize().extrude(-65).union(w0.sketch().push([(-12,58)]).circle(42).push([(-12,58.5)]).rect(64,29,mode='s').finalize().extrude(9)).union(w1.workplane(offset=-64/2).moveTo(54,-37).cylinder(64,4))