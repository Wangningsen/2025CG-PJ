import cadquery as cq
w0=cq.Workplane('YZ',origin=(5,0,0))
r=w0.sketch().push([(52,-8)]).circle(23).push([(38,3)]).circle(7,mode='s').finalize().extrude(-35).union(w0.workplane(offset=8/2).moveTo(50.5,-9).box(99,36,8)).union(w0.sketch().push([(-49,0)]).circle(51).circle(48,mode='s').finalize().extrude(25))