import cadquery as cq
w0=cq.Workplane('YZ',origin=(15,0,0))
r=w0.sketch().push([(-49,-77)]).rect(102,12).circle(2,mode='s').push([(45.5,26.5)]).rect(109,113).finalize().extrude(-31)