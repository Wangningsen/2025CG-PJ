import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
r=w0.sketch().segment((-100,-40),(2,-92)).segment((44,-13)).segment((100,-4)).segment((88,66)).segment((36,56)).segment((-33,92)).close().assemble().finalize().extrude(-32)