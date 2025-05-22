import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().arc((-31,-61),(-5,-62),(17,-67)).arc((6,67),(-31,-61)).assemble().finalize().extrude(200)