import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-99))
r=w0.sketch().push([(0,-74)]).rect(112,52).push([(0,73)]).rect(112,54).finalize().extrude(198)