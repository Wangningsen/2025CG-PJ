import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().arc((40,52),(-66,-10),(51,-41)).segment((48,-41)).segment((48,-37)).segment((53,-37)).segment((53,-40)).arc((66,9),(40,52)).assemble().finalize().extrude(-200)