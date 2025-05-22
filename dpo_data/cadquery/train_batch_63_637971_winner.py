import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-29,65),(-19,-68)).segment((29,-65)).segment((19,68)).close().assemble().rect(2,26,mode='s').finalize().extrude(-200)