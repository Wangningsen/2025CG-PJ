import cadquery as cq
w0=cq.Workplane('YZ',origin=(80,0,0))
w1=cq.Workplane('YZ',origin=(77,0,0))
r=w0.sketch().arc((77,30),(-10,-70),(81,26)).segment((98,45)).segment((77,73)).close().assemble().push([(32.5,-19)]).rect(35,120,mode='s').finalize().extrude(-125).union(w1.workplane(offset=-157/2).moveTo(-38,25).cylinder(157,62))