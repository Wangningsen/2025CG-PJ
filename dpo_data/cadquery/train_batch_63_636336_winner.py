import cadquery as cq
w0=cq.Workplane('YZ',origin=(5,0,0))
r=w0.sketch().push([(0,-55)]).circle(45).push([(33.5,69.5)]).rect(15,61).finalize().extrude(-9)