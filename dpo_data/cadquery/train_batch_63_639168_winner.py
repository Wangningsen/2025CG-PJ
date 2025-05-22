import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,5))
r=w0.sketch().push([(-47.5,80.5)]).rect(37,39).push([(-48,80)]).rect(34,6,mode='s').finalize().extrude(-25).union(w0.sketch().push([(-22,-73)]).circle(27).push([(28,0)]).circle(38).finalize().extrude(15))