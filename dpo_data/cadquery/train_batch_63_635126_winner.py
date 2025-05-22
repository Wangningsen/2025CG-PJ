import cadquery as cq
w0=cq.Workplane('YZ',origin=(-57,0,0))
r=w0.sketch().segment((-97,-23),(-3,-100)).segment((97,23)).segment((3,100)).close().assemble().finalize().extrude(114)