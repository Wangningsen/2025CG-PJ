import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,35,0))
w1=cq.Workplane('YZ',origin=(45,0,0))
r=w0.sketch().push([(-1,7)]).rect(30,28).push([(-1,8)]).rect(12,14,mode='s').finalize().extrude(10).union(w1.sketch().segment((-100,-51),(-27,-51)).arc((92,33),(-46,-14)).segment((-100,-14)).close().assemble().finalize().extrude(-89))