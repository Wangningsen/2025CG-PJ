import cadquery as cq
w0=cq.Workplane('YZ',origin=(-55,0,0))
w1=cq.Workplane('YZ',origin=(-21,0,0))
r=w0.sketch().segment((77,37),(81,43)).segment((77,45)).close().assemble().finalize().extrude(4).union(w0.sketch().segment((75,37),(87,37)).arc((81,40),(75,44)).close().assemble().finalize().extrude(120)).union(w0.workplane(offset=120/2).moveTo(45,0).cylinder(120,55)).union(w1.sketch().push([(-55,1.5)]).rect(90,67).push([(-97,16.5)]).rect(4,3,mode='s').finalize().extrude(-44))