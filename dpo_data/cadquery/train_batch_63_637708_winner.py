import cadquery as cq
w0=cq.Workplane('YZ',origin=(-57,0,0))
r=w0.sketch().push([(0,90.5)]).rect(106,19).push([(-22,84.5)]).rect(16,7,mode='s').finalize().extrude(-28).union(w0.sketch().segment((1,-100),(18,-100)).segment((18,-4)).segment((3,-4)).arc((-46,2),(1,-11)).close().assemble().finalize().extrude(142))