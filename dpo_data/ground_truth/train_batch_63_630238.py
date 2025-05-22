import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((56,-35),(52,0),(56,35)).arc((-56,0),(56,-35)).assemble().finalize().extrude(-200)