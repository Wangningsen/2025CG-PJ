import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
r=w0.sketch().push([(-5,-59)]).rect(178,82).push([(76,82)]).circle(18).finalize().extrude(-16)