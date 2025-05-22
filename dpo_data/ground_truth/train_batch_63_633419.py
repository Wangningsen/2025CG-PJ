import cadquery as cq
w0=cq.Workplane('YZ',origin=(-9,0,0))
w1=cq.Workplane('XY',origin=(0,0,10))
r=w0.sketch().arc((-11,-93),(-7,-100),(-1,-95)).arc((6,-38),(-11,-93)).assemble().finalize().extrude(15).union(w1.sketch().push([(5,23)]).circle(4).circle(3,mode='s').finalize().extrude(90))