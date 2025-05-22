import cadquery as cq
w0=cq.Workplane('YZ',origin=(80,0,0))
w1=cq.Workplane('YZ',origin=(77,0,0))
r=w0.sketch().arc((-30,-39),(67,-78),(80,29)).segment((97,45)).segment((78,72)).segment((47,51)).arc((37,47),(28,40)).arc((-24,17),(-30,-39)).assemble().push([(32.5,-19)]).rect(35,120,mode='s').finalize().extrude(-126).union(w1.workplane(offset=-157/2).moveTo(-38,25).cylinder(157,62))