import cadquery as cq
w0=cq.Workplane('YZ',origin=(-39,0,0))
w1=cq.Workplane('XY',origin=(0,0,0))
r=w0.sketch().segment((-20,18),(-8,18)).segment((-8,28)).arc((-14,26),(-20,25)).close().assemble().finalize().extrude(-46).union(w0.workplane(offset=124/2).moveTo(26.5,42.5).box(39,115,124)).union(w1.sketch().push([(-10.5,-14.5)]).rect(75,63).push([(-3.5,-33.5)]).rect(13,11,mode='s').finalize().extrude(-100))