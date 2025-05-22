import cadquery as cq
w0=cq.Workplane('YZ',origin=(-16,0,0))
r=w0.sketch().segment((-100,-40),(3,-92)).segment((43,-14)).segment((100,-4)).segment((88,66)).segment((36,57)).segment((-33,92)).close().assemble().finalize().extrude(32)