import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().arc((-77,-58),(-46,-72),(-20,-94)).arc((52,81),(-77,-58)).assemble().finalize().extrude(-200)