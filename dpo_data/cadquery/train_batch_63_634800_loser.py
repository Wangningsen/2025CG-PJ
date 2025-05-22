import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-6,0))
w1=cq.Workplane('YZ',origin=(-5,0,0))
r=w0.sketch().arc((-39,22),(28,36),(-23,83)).arc((-91,71),(-39,22)).assemble().push([(-3,-74)]).circle(26).finalize().extrude(16).union(w1.sketch().arc((-83,52),(-75,36),(-61,26)).arc((-18,-9),(28,19)).arc((83,59),(20,85)).arc((-23,75),(-49,38)).arc((-66,46),(-83,52)).assemble().finalize().extrude(3))