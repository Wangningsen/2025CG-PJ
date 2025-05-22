import cadquery as cq
w0=cq.Workplane('YZ',origin=(-74,0,0))
r=w0.sketch().arc((-84,41),(-90,-30),(-35,-74)).segment((-35,-96)).segment((-6,-96)).segment((-6,-74)).arc((24,-61),(46,-37)).arc((96,43),(7,71)).arc((1,73),(-6,74)).segment((-6,96)).segment((-35,96)).segment((-35,74)).arc((-60,65),(-80,47)).arc((-98,56),(-84,41)).assemble().finalize().extrude(149)