import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,61))
r=w0.sketch().arc((-62,7),(-70,-40),(-24,-49)).arc((-24,-44),(-19,-46)).arc((-15,-41),(-11,-35)).segment((38,-35)).segment((38,100)).segment((-62,100)).close().assemble().finalize().extrude(-144).union(w0.workplane(offset=22/2).moveTo(1.5,-75).box(149,50,22))