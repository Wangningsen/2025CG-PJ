import cadquery as cq
w0=cq.Workplane('YZ',origin=(81,0,0))
r=w0.sketch().push([(-16,2)]).circle(84).push([(85.5,-11)]).rect(29,150).finalize().extrude(-162)