import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,62))
r=w0.sketch().push([(-97,7)]).circle(3).push([(87,0)]).circle(13).finalize().extrude(-124)