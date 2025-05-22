import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().arc((40,53),(-66,-7),(50,-44)).segment((48,-44)).segment((48,-37)).segment((55,-37)).arc((67,2),(52,41)).arc((43,44),(40,53)).assemble().finalize().extrude(200)