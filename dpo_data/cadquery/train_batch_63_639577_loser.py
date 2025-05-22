import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,92,0))
r=w0.sketch().rect(200,138).push([(43,-53.5)]).rect(102,23,mode='s').push([(43,-53)]).circle(13).finalize().extrude(-184)