import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-66,58),(-45,41)).segment((-15,37)).segment((29,5)).segment((-6,5)).segment((36,-34)).segment((43,-25)).segment((65,-60)).arc((33,27),(-66,58)).assemble().finalize().extrude(-200)