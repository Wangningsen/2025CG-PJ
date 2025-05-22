import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().arc((-75,-60),(-41,-75),(-14,-96)).arc((47,84),(-75,-60)).assemble().finalize().extrude(200)