import cadquery as cq
w0=cq.Workplane('YZ',origin=(-56,0,0))
w1=cq.Workplane('YZ',origin=(-22,0,0))
r=w0.sketch().segment((77,37),(77,45)).arc((5,-38),(86,37)).close().assemble().finalize().extrude(121).union(w1.sketch().push([(-55,1.5)]).rect(90,67).push([(-97.5,19)]).rect(3,4,mode='s').finalize().extrude(-44))