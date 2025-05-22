import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,19))
w1=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((70,66),(94,24)).arc((96,54),(70,66)).assemble().finalize().extrude(-107).union(w0.workplane(offset=69/2).moveTo(-43,-7.5).box(8,59,69)).union(w1.workplane(offset=118/2).moveTo(-35.5,37).box(61,24,118))