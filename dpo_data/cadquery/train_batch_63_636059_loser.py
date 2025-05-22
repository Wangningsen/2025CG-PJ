import cadquery as cq
w0=cq.Workplane('YZ',origin=(10,0,0))
r=w0.sketch().push([(-99,71.5)]).rect(2,57).push([(-9,21)]).circle(11).push([(16,71.5)]).rect(2,57).push([(68,-36)]).rect(64,128).finalize().extrude(-20)