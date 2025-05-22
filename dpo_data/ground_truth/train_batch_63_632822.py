import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().arc((44,80),(-76,-55),(88,20)).arc((86,64),(44,80)).assemble().push([(53,40)]).circle(23,mode='s').finalize().extrude(-200)