import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().arc((-65,41),(55,-53),(-41,65)).arc((-61,61),(-65,41)).assemble().finalize().extrude(-200)