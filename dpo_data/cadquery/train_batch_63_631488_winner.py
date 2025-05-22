import cadquery as cq
w0=cq.Workplane('YZ',origin=(32,0,0))
r=w0.sketch().push([(0,-34)]).circle(66).circle(6,mode='s').push([(31,65)]).circle(35).finalize().extrude(-65)